def ChkNum(X):
    result = X % 2
    if result == 0:
        print("Output:Even Number")
    else:
        print("Output:Odd Number")
    return result

def main():
    print("Input:")
    no = int(input())

    ans = ChkNum(no)
  

if __name__ == "__main__":
    main()