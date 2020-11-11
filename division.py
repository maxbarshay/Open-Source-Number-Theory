def divide(a, b, disp = False):
    whole = a // b
    rem = a % b
    if disp:
        print(str(a) + " * " + str(whole) + " + " +  str(rem))
    return b, rem


def main():
    a = int(input("Dividend: "))
    b = int(input("Divisor: "))
    divide(a, b, True)

if __name__ == "__main__":
    main()