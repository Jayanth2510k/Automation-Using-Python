from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X = df[['quantity', 'unit_price']]
    y = df['revenue']
    model = RandomForestRegressor()
    model.fit(X, y)
    df['predicted_revenue'] = model.predict(X)
    return df, model

if __name__ == "__main__":
    from transform_data import transform_data
    from extract_data import extract_data
    df = transform_data(extract_data())
    df, model = train_model(df)
    print(df[['revenue', 'predicted_revenue']].head())
