import pandas as pd

#Starts to transfomr from basic transformed dataset
csv_file='Transformation\Transformed DataSet\Exito_smrtphones_basic_transf.csv'
df = pd.read_csv(csv_file)

#Transform % off and price

filter_discount_df  = df[['Discount', 'Discount Price']]

folder_path = 'Transformation\Transformed DataSet'

file_name = 'discount.csv'

new_csv_file_path = folder_path + file_name

filter_discount_df.to_csv(new_csv_file_path, index=True)

