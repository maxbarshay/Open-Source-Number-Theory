import math

def fermfact(n):

    done = False
    
    k = math.ceil(math.sqrt(n))


    while not done:

        val = k ** 2 - n
        
        if math.sqrt(val).is_integer():

            done = True

        else:

            k += 1


        print(val)

    print("k", k)

    root_val = int(math.sqrt(val))

    print("val", root_val)

    first = k + root_val

    second = k - root_val

    print("first", first)

    print("second", second)


def main():

    fermfact(3658)


if __name__ == '__main__':
    main()