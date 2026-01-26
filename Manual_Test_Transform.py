from etl.extract import extract_data
from etl.transform import transform_data

df=extract_data()
df_transformed=transform_data(df)

print(df_transformed)
