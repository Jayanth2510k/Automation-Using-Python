import schedule
import time
from generate_report import generate_report
from model_train import train_model
from transform_data import transform_data
from extract_data import extract_data

def job():
    df = extract_data()
    df = transform_data(df)
    df, _ = train_model(df)
    generate_report(df)
    print("Report generated successfully!")

schedule.every().day.at("09:00").do(job)

if __name__ == "__main__":
    print("Scheduler started. Waiting to run job...")
    while True:
        schedule.run_pending()
        time.sleep(60)

