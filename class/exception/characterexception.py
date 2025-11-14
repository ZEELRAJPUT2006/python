class informationcheckedException(Exception):
    pass

# class information:

def acceptchecked(str):
    if str.isalpha():
        print("your information is correct")
    else:
        raise informationcheckedException()
        
acceptchecked("abcd123")