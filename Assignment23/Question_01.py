import pandas as pd

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Data is : ",df)

    print("Shape of data : ",df.shape)

    print("Column in data : ")
    df.info()

    print("Datatype is : ")
    print(df.dtypes)


def main():
    Dataframe()

if __name__ == "__main__":
    main()