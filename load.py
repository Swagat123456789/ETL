from pathlib import Path

from pathlib import Path

# Fixed base path for your system
BASE_PATH = Path(
    r"C:\Users\jwy1kor\Desktop\Regression Test\BSWRT\LOcal Test"
)
def load_data(df):
    target_file=BASE_PATH /"data"/"target_data.csv"
    df.to_csv(target_file,index=False)
    return target_file
    