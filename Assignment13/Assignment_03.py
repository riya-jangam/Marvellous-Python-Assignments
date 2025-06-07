class Numbers:

    def __init__ (self):
        self.Value = int(input("Enter Number : "))

    def ChkPrime(self):
        factor = 1
        for i in range (1,self.Value+1):
            if self.Value%i == 0 :
                factor *= i
        if factor == self.Value :
            return True
        else :
            return False

    def Factor(self):
        result=[]
        for i in range(1,self.Value):
            if (self.Value%i==0):
                result.append(i)
        print("Factors are : ",result)

    def SumFactor(self):
        result=0
        for i in range(1,self.Value):
            if (self.Value%i==0):
                result=result+i
        print("Sum of factors : ",result)

    def ChkPerfect(self):
        result=0
        for i in range(1,self.Value):
            if (self.Value%i==0):
                result=result+i
        return self.Value == result
        
def main ():
    obj1= Numbers()
    ret1 = obj1.ChkPrime()
    print("Prime : ",ret1)
    obj1.Factor()
    obj1.SumFactor()
    ret2 = obj1.ChkPerfect()
    print("Perfect : ",ret2)

if __name__ == "__main__":
    main()