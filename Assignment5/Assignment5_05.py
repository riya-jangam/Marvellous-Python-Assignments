def check(no):
    if no%2 == 0 :
        print(no," is an even number ")
    else:
        print(no," is an odd number ")


def main():
    A = int(input("Enter a number : "))

    check(A)

if __name__=="__main__":
    main()