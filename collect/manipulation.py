import pandas as pd
import numpy as np
from ast import pattern
import re


def extract_year(prod_nome):
    match = re.search(r'(\d{4}(?:-\d{2})?)', prod_nome)
    if match:
        return match.groups(1)
    return None

def clean_product_name_year(prod_name):
    pattern = r'\s*\d{4}(?:-\d{2})?.*$'
    cleaned_name = re.sub(pattern, '', prod_name)
    return cleaned_name.strip()

def clean_product_name_type(prod_name):
    pattern = r"(home|away|third)"
    cleaned_name = re.sub(pattern, '', prod_name)
    return cleaned_name.strip()

def product_type(prod_name):
    pattern = r"(home|away|third)"
    match = re.search(pattern, prod_name)
    if match:
        return match.group(1)
    return None

def clean_price_name(data):
    data['nome'] = data['nome'].str.lower()
    data['preço'] = data['preço'].str.replace('R$', '').str.replace(',', '.').astype(float)
    return data 

def reorder_attributes(data):  
    order = ['nome','tipo','temporada','preço']
    return data[order]
 
def shirt_manipulation():
    raw_data = pd.read_csv('../data/raw_data.csv')
    data = clean_price_name(raw_data)
    data1 = pd.DataFrame(data)
    data1['nome'] = data['nome'].apply(clean_product_name_year)
    data1['temporada'] = data['nome'].apply(extract_year).str.get(0)
    data1['tipo'] = data['nome'].apply(product_type)
    data1['nome'] = data1['nome'].apply(clean_product_name_type)
    
    data_end = reorder_attributes(data1)
    data_end.to_csv('../dashboard_camisetas/data/data_camisetas.csv', index=False)


def main():
    shirt_manipulation()
    #team_manipulation()




if __name__ == "__main__":
    main()