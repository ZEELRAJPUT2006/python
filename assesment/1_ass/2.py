#!/usr/bin/env python3
"""
libradesk.py
Compact single-file prototype for LibraDesk (Advanced Python assessment).
Run: python libradesk.py
"""

import os
import re
import csv
import sqlite3
from datetime import datetime, timedelta
from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# ---------------------------
# Exceptions
# ---------------------------
class LibraryError(Exception):
    pass

class BookNotAvailableError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class BookNotFoundError(LibraryError):
    pass

# ---------------------------
# Data models
# ---------------------------
@dataclass
class Book:
    id: int
    title: str
    author: str
    genre: str
    isbn: str
    available: bool

@dataclass
class Member:
    id: int
    name: str
    email: str
    role: str  # 'member' | 'librarian' | 'admin'

# ---------------------------
# Library core (DB + operations)
# ---------------------------
DB_FILE = "libradesk.db"
INVOICE_DIR = "invoices"

class Library:
    FINE_PER_DAY = 5.0  # currency units per day overdue

    def __init__(self, db_path=DB_FILE):
        os.makedirs(INVOICE_DIR, exist_ok=True)
        self.conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            genre TEXT,
            isbn TEXT UNIQUE,
            available INTEGER DEFAULT 1
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            role TEXT DEFAULT 'member'
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS borrow_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            book_id INTEGER,
            borrow_date TIMESTAMP,
            due_date TIMESTAMP,
            return_date TIMESTAMP,
            FOREIGN KEY(member_id) REFERENCES members(id),
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
        """)
        # Create a default admin and librarian for demonstration:
        c.execute("INSERT OR IGNORE INTO members (id, name, email, role) VALUES (1, 'Admin', 'admin@libra', 'admin')")
        c.execute("INSERT OR IGNORE INTO members (id, name, email, role) VALUES (2, 'Librarian', 'librarian@libra', 'librarian')")
        self.conn.commit()

    # ----- Book methods -----
    def add_book(self, title, author, genre, isbn):
        c = self.conn.cursor()
        try:
            c.execute("INSERT INTO books (title, author, genre, isbn, available) VALUES (?, ?, ?, ?, 1)",
                      (title, author, genre, isbn))
            self.conn.commit()
            return c.lastrowid
        except sqlite3.IntegrityError as e:
            raise LibraryError("ISBN already exists") from e

    def update_book_availability(self, book_id, available: bool):
        c = self.conn.cursor()
        c.execute("UPDATE books SET available = ? WHERE id = ?", (1 if available else 0, book_id))
        self.conn.commit()

    def get_book(self, book_id) -> Book:
        c = self.conn.cursor()
        c.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = c.fetchone()
        if not row:
            raise BookNotFoundError(f"Book id {book_id} not found")
        return Book(row['id'], row['title'], row['author'], row['genre'], row['isbn'], bool(row['available']))

    def search_books(self, pattern, field='title'):
        # pattern is a regex, field in ('title','author','genre')
        if field not in ('title','author','genre'):
            field = 'title'
        c = self.conn.cursor()
        # naive: fetch candidates and filter in Python using re (sqlite doesn't support full-featured regex reliably)
        c.execute(f"SELECT * FROM books")
        rows = c.fetchall()
        prog = re.compile(pattern, re.IGNORECASE)
        result = []
        for r in rows:
            if r[field] and prog.search(r[field]):
                result.append(Book(r['id'], r['title'], r['author'], r['genre'], r['isbn'], bool(r['available'])))
        return result

    # ----- Member methods -----
    def add_member(self, name, email, role='member'):
        c = self.conn.cursor()
        try:
            c.execute("INSERT INTO members (name, email, role) VALUES (?, ?, ?)", (name, email, role))
            self.conn.commit()
            return c.lastrowid
        except sqlite3.IntegrityError as e:
            raise LibraryError("Email already exists") from e

    def get_member(self, member_id) -> Member:
        c = self.conn.cursor()
        c.execute("SELECT * FROM members WHERE id = ?", (member_id,))
        r = c.fetchone()
        if not r:
            raise MemberNotFoundError(f"Member id {member_id} not found")
        return Member(r['id'], r['name'], r['email'], r['role'])

    def find_member_by_email(self, email):
        c = self.conn.cursor()
        c.execute("SELECT * FROM members WHERE email = ?", (email,))
        r = c.fetchone()
        if not r: return None
        return Member(r['id'], r['name'], r['email'], r['role'])

    # ----- Borrowing -----
    def borrow_book(self, member_id, book_id, days=14):
        book = self.get_book(book_id)
        if not book.available:
            raise BookNotAvailableError("Book currently not available")
        member = self.get_member(member_id)
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=days)
        c = self.conn.cursor()
        c.execute("""INSERT INTO borrow_history (member_id, book_id, borrow_date, due_date, return_date)
                     VALUES (?, ?, ?, ?, NULL)""", (member_id, book_id, borrow_date, due_date))
        self.update_book_availability(book_id, False)
        self.conn.commit()
        return c.lastrowid, due_date

    def return_book(self, history_id):
        c = self.conn.cursor()
        c.execute("SELECT * FROM borrow_history WHERE id = ?", (history_id,))
        r = c.fetchone()
        if not r:
            raise LibraryError("Borrow record not found")
        if r['return_date'] is not None:
            raise LibraryError("Book already returned")
        return_date = datetime.now()
        c.execute("UPDATE borrow_history SET return_date = ? WHERE id = ?", (return_date, history_id))
        # mark book available
        self.update_book_availability(r['book_id'], True)
        self.conn.commit()
        # calculate fine
        due_date = datetime.fromisoformat(r['due_date'])
        days_overdue = (return_date - due_date).days
        fine = max(0, days_overdue * Library.FINE_PER_DAY)
        return fine, days_overdue

    def list_overdue(self):
        c = self.conn.cursor()
        now = datetime.now()
        c.execute("""SELECT b.id AS hist_id, m.id AS member_id, m.name, m.email, bo.title, br.due_date
                     FROM borrow_history br
                     JOIN members m ON br.member_id = m.id
                     JOIN books bo ON br.book_id = bo.id
                     WHERE br.return_date IS NULL""")
        rows = c.fetchall()
        out = []
        for r in rows:
            due = datetime.fromisoformat(r['due_date'])
            if due < now:
                days = (now - due).days
                fine = days * Library.FINE_PER_DAY
                out.append({'history_id': r['hist_id'], 'member_id': r['member_id'], 'name': r['name'],
                            'email': r['email'], 'title': r['title'], 'due_date': due, 'days_overdue': days, 'fine': fine})
        return out

    def most_borrowed(self, limit=10):
        c = self.conn.cursor()
        c.execute("""SELECT book_id, COUNT(*) as times FROM borrow_history
                     GROUP BY book_id ORDER BY times DESC LIMIT ?""", (limit,))
        rows = c.fetchall()
        result = []
        for r in rows:
            try:
                b = self.get_book(r['book_id'])
                result.append({'book': b, 'times': r['times']})
            except BookNotFoundError:
                continue
        return result

    # ----- Borrow history listing for a member -----
    def member_history(self, member_id):
        c = self.conn.cursor()
        c.execute("""SELECT br.id, bo.title, br.borrow_date, br.due_date, br.return_date
                     FROM borrow_history br JOIN books bo ON br.book_id = bo.id
                     WHERE br.member_id = ? ORDER BY br.borrow_date DESC""", (member_id,))
        return c.fetchall()

    # ----- Invoice generation and file saving -----
    def generate_invoice_text(self, member_name, book_title, borrow_date, due_date, return_date, fine):
        lines = []
        lines.append("---- LibraDesk Invoice ----")
        lines.append(f"Member: {member_name}")
        lines.append(f"Book: {book_title}")
        lines.append(f"Borrowed: {borrow_date}")
        lines.append(f"Due: {due_date}")
        lines.append(f"Returned: {return_date}")
        lines.append(f"Fine: {fine:.2f}")
        tax = fine * 0.18  # 18% tax example
        lines.append(f"Tax (18%): {tax:.2f}")
        lines.append(f"Total: {fine + tax:.2f}")
        return "\n".join(lines)

    def save_invoice(self, filename, content):
        path = os.path.join(INVOICE_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

# ---------------------------
# Minimal GUI using Tkinter
# ---------------------------
class App:
    def __init__(self, master):
        self.master = master
        master.title("LibraDesk Prototype")
        master.geometry("800x520")
        self.library = Library()

        self.current_user = None  # Member dataclass

        self._build_login()

    def _build_login(self):
        for w in self.master.winfo_children(): w.destroy()
        frame = ttk.Frame(self.master, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="LibraDesk Login", font=("TkDefaultFont", 16)).pack(pady=10)
        self.email_var = tk.StringVar()
        ttk.Label(frame, text="Email:").pack(anchor=tk.W, padx=10)
        ttk.Entry(frame, textvariable=self.email_var, width=40).pack(padx=10, pady=5)
        ttk.Button(frame, text="Login (demo)", command=self.handle_login).pack(pady=10)
        ttk.Separator(frame).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Create Demo Member", command=self.create_demo_member).pack()

    def handle_login(self):
        email = self.email_var.get().strip()
        if not email:
            messagebox.showwarning("Login", "Enter email (use admin@libra or librarian@libra or create member).")
            return
        user = self.library.find_member_by_email(email)
        if not user:
            messagebox.showerror("Login error", "No user with that email. Create a member first.")
            return
        self.current_user = user
        self._build_dashboard()

    def create_demo_member(self):
        # creates a simple member for testing
        name = f"Member{int(datetime.now().timestamp())%1000}"
        email = f"{name.lower()}@example.com"
        mid = self.library.add_member(name, email, role='member')
        messagebox.showinfo("Member created", f"Created {name} with email {email}")

    def _build_dashboard(self):
        for w in self.master.winfo_children(): w.destroy()
        top = ttk.Frame(self.master, padding=6)
        top.pack(fill=tk.X)
        ttk.Label(top, text=f"Logged in as: {self.current_user.name} ({self.current_user.role})").pack(side=tk.LEFT)
        ttk.Button(top, text="Logout", command=self._build_login).pack(side=tk.RIGHT)

        # Role-based dashboard options
        main = ttk.Frame(self.master, padding=10)
        main.pack(fill=tk.BOTH, expand=True)

        if self.current_user.role == 'admin':
            self._admin_view(main)
        elif self.current_user.role == 'librarian':
            self._librarian_view(main)
        else:
            self._member_view(main)

    def _admin_view(self, parent):
        # Admin: manage books, view reports
        left = ttk.Frame(parent)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        ttk.Label(left, text="Admin - Books").pack()
        self._book_form(left)
        ttk.Button(left, text="View Most Borrowed", command=self._show_most_borrowed).pack(pady=5)

        right = ttk.Frame(parent)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        ttk.Label(right, text="Reports").pack()
        ttk.Button(right, text="Overdue List", command=self._show_overdue).pack(pady=2)
        ttk.Button(right, text="All Books", command=self._show_all_books).pack(pady=2)

    def _librarian_view(self, parent):
        left = ttk.Frame(parent)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        ttk.Label(left, text="Librarian - Members & Borrowing").pack()
        self._member_form(left)
        ttk.Button(left, text="Borrow Book (open form)", command=self._borrow_form).pack(pady=3)
        ttk.Button(left, text="Return Book (select history id)", command=self._return_form).pack(pady=3)

        right = ttk.Frame(parent)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        ttk.Label(right, text="Search Books (regex)").pack()
        self._search_form(right)

    def _member_view(self, parent):
        ttk.Label(parent, text="Member dashboard — view/search books").pack(pady=5)
        self._search_form(parent)
        ttk.Button(parent, text="My Borrow History", command=self._show_my_history).pack(pady=5)

    # ---- small reusable UI pieces ----
    def _book_form(self, container):
        f = ttk.Frame(container); f.pack(pady=6)
        self.btitle = tk.StringVar(); self.bauthor = tk.StringVar(); self.bgenre = tk.StringVar(); self.bisbn = tk.StringVar()
        ttk.Label(f, text="Title").grid(row=0,column=0)
        ttk.Entry(f, textvariable=self.btitle).grid(row=0,column=1)
        ttk.Label(f, text="Author").grid(row=1,column=0)
        ttk.Entry(f, textvariable=self.bauthor).grid(row=1,column=1)
        ttk.Label(f, text="Genre").grid(row=2,column=0)
        ttk.Entry(f, textvariable=self.bgenre).grid(row=2,column=1)
        ttk.Label(f, text="ISBN").grid(row=3,column=0)
        ttk.Entry(f, textvariable=self.bisbn).grid(row=3,column=1)
        ttk.Button(f, text="Add Book", command=self._add_book).grid(row=4,column=0,columnspan=2,pady=6)

    def _member_form(self, container):
        f = ttk.Frame(container); f.pack(pady=6)
        self.mname = tk.StringVar(); self.memail = tk.StringVar(); self.mrole = tk.StringVar(value='member')
        ttk.Label(f, text="Name").grid(row=0,column=0)
        ttk.Entry(f, textvariable=self.mname).grid(row=0,column=1)
        ttk.Label(f, text="Email").grid(row=1,column=0)
        ttk.Entry(f, textvariable=self.memail).grid(row=1,column=1)
        ttk.Label(f, text="Role").grid(row=2,column=0)
        ttk.Combobox(f, values=['member','librarian','admin'], textvariable=self.mrole).grid(row=2,column=1)
        ttk.Button(f, text="Add Member", command=self._add_member).grid(row=3,column=0,columnspan=2,pady=6)

    def _search_form(self, container):
        f = ttk.Frame(container); f.pack(pady=6)
        self.search_field = tk.StringVar(value='title'); self.search_pattern = tk.StringVar()
        ttk.Combobox(f, values=['title','author','genre'], textvariable=self.search_field).grid(row=0,column=0)
        ttk.Entry(f, textvariable=self.search_pattern, width=30).grid(row=0,column=1)
        ttk.Button(f, text="Search", command=self._do_search).grid(row=0,column=2)

    # ---- actions ----
    def _add_book(self):
        try:
            bid = self.library.add_book(self.btitle.get(), self.bauthor.get(), self.bgenre.get(), self.bisbn.get())
            messagebox.showinfo("Book added", f"Book id {bid} added")
            self.btitle.set(self.bauthor.set(self.bgenre.set(self.bisbn.set(""))))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _add_member(self):
        try:
            mid = self.library.add_member(self.mname.get(), self.memail.get(), self.mrole.get())
            messagebox.showinfo("Member added", f"Member id {mid} added")
            self.mname.set(""); self.memail.set("")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _do_search(self):
        patt = self.search_pattern.get().strip()
        fld = self.search_field.get()
        if not patt:
            messagebox.showwarning("Search", "Enter a regex pattern.")
            return
        try:
            results = self.library.search_books(patt, field=fld)
        except re.error as e:
            messagebox.showerror("Regex error", str(e))
            return
        self._show_books(results)

    def _show_books(self, book_list=None):
        if book_list is None:
            c = self.library.conn.cursor()
            c.execute("SELECT * FROM books")
            rows = c.fetchall()
            book_list = [Book(r['id'], r['title'], r['author'], r['genre'], r['isbn'], bool(r['available'])) for r in rows]
        win = tk.Toplevel(self.master); win.title("Books")
        tree = ttk.Treeview(win, columns=("id","title","author","genre","isbn","avail"), show='headings')
        for h in ("id","title","author","genre","isbn","avail"): tree.heading(h, text=h)
        for b in book_list:
            tree.insert("", "end", values=(b.id, b.title, b.author, b.genre, b.isbn, "Yes" if b.available else "No"))
        tree.pack(fill=tk.BOTH, expand=True)

    def _show_all_books(self):
        self._show_books()

    def _show_overdue(self):
        overdue = self.library.list_overdue()
        win = tk.Toplevel(self.master); win.title("Overdue")
        tree = ttk.Treeview(win, columns=("hist","member","title","due","days","fine"), show='headings')
        for h in ("hist","member","title","due","days","fine"): tree.heading(h, text=h)
        for o in overdue:
            tree.insert("", "end", values=(o['history_id'], o['name'], o['title'], o['due_date'].strftime("%Y-%m-%d"), o['days_overdue'], f"{o['fine']:.2f}"))
        tree.pack(fill=tk.BOTH, expand=True)

    def _show_most_borrowed(self):
        arr = self.library.most_borrowed()
        win = tk.Toplevel(self.master); win.title("Most Borrowed")
        text = tk.Text(win, height=20); text.pack(fill=tk.BOTH, expand=True)
        for r in arr:
            b = r['book']
            text.insert(tk.END, f"{b.title} by {b.author} — borrowed {r['times']} times\n")

    def _borrow_form(self):
        win = tk.Toplevel(self.master); win.title("Borrow Book")
        ttk.Label(win, text="Member ID").grid(row=0,column=0)
        mem = tk.StringVar(); ttk.Entry(win, textvariable=mem).grid(row=0,column=1)
        ttk.Label(win, text="Book ID").grid(row=1,column=0); book = tk.StringVar(); ttk.Entry(win, textvariable=book).grid(row=1,column=1)
        ttk.Label(win, text="Days (default 14)").grid(row=2,column=0); days = tk.StringVar(value='14'); ttk.Entry(win, textvariable=days).grid(row=2,column=1)
        def do_borrow():
            try:
                m = int(mem.get()); b = int(book.get()); d = int(days.get())
                hist_id, due = self.library.borrow_book(m, b, days=d)
                messagebox.showinfo("Borrowed", f"Record {hist_id}. Due: {due.date()}")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        ttk.Button(win, text="Borrow", command=do_borrow).grid(row=3,column=0,columnspan=2,pady=6)

    def _return_form(self):
        win = tk.Toplevel(self.master); win.title("Return Book")
        ttk.Label(win, text="Borrow record ID").grid(row=0,column=0)
        hid = tk.StringVar(); ttk.Entry(win, textvariable=hid).grid(row=0,column=1)
        def do_return():
            try:
                hid_i = int(hid.get())
                fine, days = self.library.return_book(hid_i)
                msg = f"Returned. Fine: {fine:.2f} (days overdue: {days})"
                # generate simple invoice: fetch record to include details
                c = self.library.conn.cursor()
                c.execute("""SELECT br.*, m.name as mname, bo.title as btitle
                             FROM borrow_history br JOIN members m ON br.member_id=m.id JOIN books bo ON br.book_id=bo.id
                             WHERE br.id = ?""", (hid_i,))
                r = c.fetchone()
                invoice_text = self.library.generate_invoice_text(r['mname'], r['btitle'], r['borrow_date'], r['due_date'], datetime.now(), fine)
                # ask to save file
                save = messagebox.askyesno("Save invoice?", "Save invoice as text file?")
                if save:
                    fn = f"invoice_{hid_i}_{int(datetime.now().timestamp())}.txt"
                    path = self.library.save_invoice(fn, invoice_text)
                    msg += f"\nInvoice saved: {path}"
                messagebox.showinfo("Return", msg)
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        ttk.Button(win, text="Return", command=do_return).grid(row=1,column=0,columnspan=2,pady=6)

    def _show_my_history(self):
        rows = self.library.member_history(self.current_user.id)
        win = tk.Toplevel(self.master); win.title("My History")
        tree = ttk.Treeview(win, columns=("id","title","borrowed","due","returned"), show='headings')
        for h in ("id","title","borrowed","due","returned"): tree.heading(h, text=h)
        for r in rows:
            b = r['borrow_date'][:19] if r['borrow_date'] else ''
            d = r['due_date'][:19] if r['due_date'] else ''
            ret = r['return_date'][:19] if r['return_date'] else ''
            tree.insert("", "end", values=(r['id'], r['title'], b, d, ret))
        tree.pack(fill=tk.BOTH, expand=True)

# ---------------------------
# Run app
# ---------------------------
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
