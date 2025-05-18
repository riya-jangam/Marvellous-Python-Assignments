def factors_add (num): 
    Sum_factor = 0
    for i in range (1, num):
       if num % i == 0:
        Sum_factor += i
        print("Factors are :",i)
    print ("Sum of Factors : ",Sum_factor)

def main():
   no = int(input("Enter number : "))
   factors_add(no)

if __name__ == "__main__":
    main() 