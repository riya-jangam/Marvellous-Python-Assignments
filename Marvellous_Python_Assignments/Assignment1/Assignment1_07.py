def div(val):
    result = val % 5 
    return result

def main():
    print ("Enter number :")
    X =int(input())

    ans = div(X)
    
    if ans == 0:
        print ("The number is divisible by 5 _ True")
    else:
        print ("The number is not divisible by 5 _ False")

if __name__ == "__main__" :
    main()
