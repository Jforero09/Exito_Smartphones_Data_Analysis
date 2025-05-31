import pandas as pd

#Starts to transfomr from basic transformed dataset
csv_file='Transformation\Transformed DataSet\Exito_smrtphones_basic_transf.csv'
df = pd.read_csv(csv_file)

#Filter by product brand
filter_seller_df  = df[['Brand', 'Product Name']]

folder_path = 'Transformation\Transformed DataSet'

file_name = 'product.csv'

new_csv_file_path = folder_path + file_name

filter_seller_df.to_csv(new_csv_file_path, index=True)


