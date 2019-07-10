"""
m = age mother
s = age of son at his birth (=0)
n = maximum lifespan

"""



def motherson(m, n):
    s = 0
    k  = 0  #number of potential palindromes
    while m < n:
        mz = str(m).zfill(2)
        sz = str(s).zfill(2)
        if mz[0] == sz[-1] and mz[-1] == sz[0]:  # and sz[0] != '0' (if 0x <> x0 should be out)
            k = k + 1
            print("     ", k, "x", mz,sz,"palindrome")
        m = m + 1
        s = s + 1


def compare():
    n = 0
    while n < 80:
        t = 18+n
        print('Age difference = ', t, ":")
        motherson(t,99)
        n = n + 1

compare()
