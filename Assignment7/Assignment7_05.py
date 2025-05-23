def palindrome(str):
    length=len(str)
    i=0
    j=-1
    label=False
    while(i<length):
        if str[i]==str[j]:
            label=True
        i=i+1
        j=j-1
    if label==True:
        print(str,"is a palindrome")
    else:
        print(str,"is not a palindrome")

def main():
    print("enter a string: ")
    word=input()
    palindrome(word)


if __name__=="__main__":
    main()
