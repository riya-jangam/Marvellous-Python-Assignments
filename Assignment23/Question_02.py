import pandas as pd

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Data is : ",df)

    print("Descnptlve statis : ")
    print(df.describe())

def main():
    Dataframe()

if __name__ == "__main__":
    main()