import pandas as pd
import re

#Starts to transfomr from basic transformed dataset
csv_file='Transformation\Transformed DataSet\Exito_smrtphones_basic_transf.csv'
df = pd.read_csv(csv_file)

#Filter by only refurbished phones

filter__refurbi_df= df[df['Product Name'].str.contains(r'reacondicionado', case=False, regex=True)]

#Create a new column Waranty status 

filter__refurbi_df['Waranty status'] = filter__refurbi_df['Product Name'].apply(
    lambda x: 'available' if 'garantia' in str(x).lower() else 'not available'
)

#Create a new column Waranty period

def extract_warranty_period(product_name):
    match = re.search(r'(\d{1,2})\s*meses', str(product_name).lower())
    if match:
        return int(match.group(1))
    else:
        return None
filter__refurbi_df['Waranty Period (Months)'] = filter__refurbi_df['Product Name'].apply(extract_warranty_period).fillna(0).astype(int)

#Create a new column accesories included

def check_accessories(product_name):
    keywords = ['regalo', 'airpods', 'audifonos', 'cargador', 'cable']
    name_lower = str(product_name).lower()
    return 'yes' if any(kw in name_lower for kw in keywords) else 'no'

filter__refurbi_df['Accessories Included'] = filter__refurbi_df['Product Name'].apply(check_accessories)


folder_path = 'Transformation\Transformed DataSet'

file_name = 'refurbished_phones.csv'

new_csv_file_path = folder_path + file_name

filter__refurbi_df.to_csv(new_csv_file_path, index=True)