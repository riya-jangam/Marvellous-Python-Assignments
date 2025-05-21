def vote (no):
    if no >= 18 :
        print("Eligible to vote")
    else :
        print("Not Eligible to vote")

def main():
    val = int(input("Enter age : "))

    vote(val)

if __name__ == "__main__":
    main()
