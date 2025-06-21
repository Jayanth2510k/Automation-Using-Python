from sqlalchemy import create_engine
import pandas as pd

def extract_data():
    engine = create_engine('sqlite:///data/sales_sample.db')
    query = "SELECT * FROM sales_data;"
    df = pd.read_sql(query, engine)
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())
