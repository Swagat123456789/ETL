from etl.extract import extract_data
from etl.transform import transform_data

from etl.load import load_data

df=extract_data()

df_transformed=transform_data(df)

target_path=load_data(df_transformed)

print("ETL Completed Sucessfully")
print("Target File created at:",target_path)
