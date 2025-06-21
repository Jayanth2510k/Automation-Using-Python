import pandas as pd

def transform_data(df):
    df['revenue'] = df['quantity'] * df['unit_price']
    df.dropna(inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    return df

if __name__ == "__main__":
    from extract_data import extract_data
    df = extract_data()
    df = transform_data(df)
    print(df.head())
