import pandas as pd
from sqlalchemy import create_engine


# Connection with data base
engine = create_engine("mysql+pymysql://root:juanes09@localhost/exito_smartphones_db")

# Read csv and create index as PK
df_sellers = pd.read_csv(r"G:\ExitoSmartphones Data Analysis\Transformation\Transformed DataSetsellers.csv", index_col=0)
df_discount = pd.read_csv(r"G:\ExitoSmartphones Data Analysis\Transformation\Transformed DataSetdiscount.csv", index_col=0)
df_refurbish = pd.read_csv(r"G:\ExitoSmartphones Data Analysis\Transformation\Transformed DataSetrefurbished_phones.csv", index_col=0)
df_product =  pd.read_csv(r"G:\ExitoSmartphones Data Analysis\Transformation\Transformed DataSetproduct.csv", index_col=0)
df_sales = pd.read_csv(r"G:\ExitoSmartphones Data Analysis\Transformation\Transformed DataSetbasic_transformation.csv", index_col=0)

# Delete 'Unnamed: 0' Columns if they appear
df_sellers = df_sellers.loc[:, ~df_sellers.columns.str.contains('^Unnamed')]
df_discount = df_discount.loc[:, ~df_discount.columns.str.contains('^Unnamed')]
df_refurbish = df_refurbish.loc[:, ~df_refurbish.columns.str.contains('^Unnamed')]
df_product = df_product.loc[:, ~df_product.columns.str.contains('^Unnamed')]
df_sales = df_sales.loc[:, ~df_sales.columns.str.contains('^Unnamed')]



# Csv Data Base Load
df_sellers.to_sql(
    name='Seller_Dimention',
    con=engine,
    if_exists='replace',      # o 'append' si no quieres borrar la tabla
    index=True,
    index_label='seller_id',   # este será la columna PK
    method='multi' 
)

df_discount.to_sql(
    name='Discount_Dimention',
    con=engine,
    if_exists='replace',      # o 'append' si no quieres borrar la tabla
    index=True,
    index_label='discount_id',   # este será la columna PK
    method='multi' 
)

df_refurbish.to_sql(
    name='Refurbish_Dimention',
    con=engine,
    if_exists='replace',      # o 'append' si no quieres borrar la tabla
    index=True,
    index_label='refurbish_id',   # este será la columna PK
    method='multi' 
)
df_product.to_sql(
    name='Product_Dimention',
    con=engine,
    if_exists='replace',      # o 'append' si no quieres borrar la tabla
    index=True,
    index_label='product_id',   # este será la columna PK
    method='multi' 
)

df_sales.to_sql(
    name='Sale_Fact',
    con=engine,
    if_exists='replace',      # o 'append' si no quieres borrar la tabla
    index=True,
    index_label='sale_id',   # este será la columna PK
    method='multi'
)


print(df_sellers.columns)
print(df_discount.columns)
print(df_refurbish.columns)
print(df_product.columns)
print(df_sales.columns)
print("Data loaded in DB Successfully")
