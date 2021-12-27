def trian_floyd(n):

    print()
    num = 1

    for i in range(n):

        for j in range(i+1):

            if(num < 10):
                print("0", end="")
            print(num, end=" ")
            num += 1

        print()


def main():

    n = int(input())
    trian_floyd(n)


main()
