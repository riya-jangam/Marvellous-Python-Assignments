def fahrenheit(C):
    F = (C * 9/5) + 32
    degree_chr = chr(176)
    print ("Temperature in Fahrenheit :",F, f"{degree_chr}F")

def main():
    val= int(input("Enter temperature in Celsius : "))

    fahrenheit(val)
        
if __name__ == "__main__":
    main()
