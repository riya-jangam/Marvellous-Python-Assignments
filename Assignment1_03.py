def Add(X,Y):
    result = X + Y
    return result

def main():
    print("Enter Input 1 :")
    no1 = int(input())

    print("Enter Input 2 :")
    no2 = int(input())

    ans = Add(no1,no2)

    print("The Output is :",ans)


if __name__ == "__main__" :
    main()
