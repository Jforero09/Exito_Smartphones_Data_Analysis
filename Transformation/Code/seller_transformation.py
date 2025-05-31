import pandas as pd

#Starts to transfomr from basic transformed dataset
csv_file='Transformation\Transformed DataSet\Exito_smrtphones_basic_transf.csv'
df = pd.read_csv(csv_file)

#Filter by seller name
filter_seller_df  = df[['Seller']].drop_duplicates().reset_index(drop=True)


folder_path = 'Transformation\Transformed DataSet'

file_name = 'sellers.csv'

new_csv_file_path = folder_path + file_name

filter_seller_df.to_csv(new_csv_file_path, index=True)
