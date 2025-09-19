import instaloader

loader = instaloader.Instaloader()

name = input("Enter name : ")
loader.download_profile(name,profile_pic=True)