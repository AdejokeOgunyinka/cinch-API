from random import randint

def generate_otp():
    print("done")
    range_start = 10**(6-1)
    range_end = (10**6)-1
    otp = randint(range_start, range_end)
    otp = str(otp)
    print({"otp":otp})
    return otp
