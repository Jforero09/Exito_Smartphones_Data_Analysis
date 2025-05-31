#This is the basic cleansy of the original cvs

import pandas as pd

csv_file='Extraction\DataSet\Exito_smatrphones.csv'
basic_df = pd.read_csv(csv_file)


#Delete all rows with NA values
basic_df = basic_df.dropna()


#####Seller Column transformation##### 
# take out 'vendido por:'


if 'Seller' in basic_df.columns:
    basic_df['Seller'] = basic_df['Seller'].str.replace("Vendido por:", '', regex=False)   
else:
    print("Failed Transformation")

#####Name Column transformation#####
# take out 'Celular:'
string_for_delete = "Vendido por:"

if 'Product Name' in basic_df.columns:
    basic_df['Product Name'] = basic_df['Product Name'].str.replace("Celular", '', regex=False)   
  

folder_path = 'Transformation\Transformed DataSet'

file_name = 'basic_transformation.csv'

new_csv_file_path = folder_path + file_name

# Guardar el DataFrame transformado en un nuevo archivo CSV
basic_df.to_csv(new_csv_file_path, index=True)

