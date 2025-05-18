square = lambda A : 2 ** A

def main():
    num = int(input("Enter Number : "))
    
    ret = square(num)

    print("square of",num,"is",ret )

if __name__ == "__main__":
    main()