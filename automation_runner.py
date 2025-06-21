from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.model_train import train_model
from scripts.generate_report import generate_report

def run():
    df = extract_data()
    df = transform_data(df)
    df, _ = train_model(df)
    generate_report(df)
    print("Automation complete!")

if __name__ == "__main__":
    run()
