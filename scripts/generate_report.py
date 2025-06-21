import matplotlib.pyplot as plt

def generate_report(df):
    monthly_revenue = df.groupby('month')['revenue'].sum()
    monthly_revenue.plot(kind='bar', title='Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.tight_layout()
    plt.savefig('reports/revenue_forecast.png')

if __name__ == "__main__":
    from model_train import train_model
    from transform_data import transform_data
    from extract_data import extract_data
    df, _ = train_model(transform_data(extract_data()))
    generate_report(df)

