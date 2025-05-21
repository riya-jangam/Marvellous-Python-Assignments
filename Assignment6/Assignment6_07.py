max : lambda A,B : A > B

def maximum (task,values):
    result = values[0] 
    for i in values :
        if i > result :
            result = i
    print("Maximum value is : ",result)
        

def main():
    size = 5

    data =[]

    print("Enter data : ")
    for i in range (5):
        no = int(input())
        data.append(no)
    print(data)

    maximum(max,data)

if __name__ == "__main__":
    main()