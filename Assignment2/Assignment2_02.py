def pattern (no):
    for i in range (no) :
            for j in range(no):
                print("*", end ="  " )
            print()

def main ():
    print("Enter a number : ")
    num = int(input())

    pattern(num)
    
if __name__ == "__main__":
    main()