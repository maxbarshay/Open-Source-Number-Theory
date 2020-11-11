from division import divide

def gcd(a, b):
    rem = 1
    while rem != 0:
        b, rem = divide(a, b)
        a = b
        b = rem
    return a


def main():
    print("GCD and LCM and Product Calculator")
    a = int(input("First Digit: "))
    b = int(input("Second Digit: "))
    product = a * b
    mygcd = gcd(a, b)
    print("The GCD is: " + str(mygcd))
    print("The LCM is: " + str(product // mygcd))
    print("The Product is: " + str(product))



if __name__ == "__main__":
    main()