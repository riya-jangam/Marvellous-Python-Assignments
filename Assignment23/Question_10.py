import pandas as pd

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Data is : ")
    print(df)


    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    print("New Data is : ")
    print(df)

    
    replace_df = df.replace('Pooja','Puja',inplace=True)
    print("Replaced data : ")
    print(df)

    drop_df = df.drop(['English'], axis=1,inplace=True)
    print("Dropped data column : ")
    print(df)


def main():
    Dataframe()

if __name__ == "__main__":
    main()