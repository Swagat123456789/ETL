import pandas as pd
from pathlib import Path

Base_Path=Path(r'C:\Users\jwy1kor\Desktop\Regression Test\BSWRT\LOcal Test')

def extract_data():
    "Extract data from the source CSV"

    source_file = Base_Path / 'data' / 'source_data.csv'
    df = pd.read_csv(source_file)
    return df