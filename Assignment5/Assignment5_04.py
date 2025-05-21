def check(no1,no2,no3):
    if (no1>no2):
        print ("Largest number is : ",no1)
    elif(no2>no3):
        print("Largest number is : ",no2)
    else:
        print("Largest number is : ",no3)


def main():
    n1 = int(input("Enter value 1 :"))
    n2 = int(input("Enter value 2 :"))
    n3 = int(input("Enter value 3 :"))

    check(n1,n2,n3)

if __name__ == "__main__":
    main()