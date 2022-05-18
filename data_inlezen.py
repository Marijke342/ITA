import pandas as pd

file2021 = '/home/marijke/Documents/Finances/Bankoverzichten/ABN_34_2021.ods'
file2022='/home/marijke/Documents/Finances/Bankoverzichten/ABN_34_2022.ods'
data = pd.concat([pd.read_excel(file2021), pd.read_excel(file2022)])
data.insert(0, 'Rekening', 'ABN_34')
data.rename(columns = {'Transactiedatum':'Datum', 'Transactiebedrag':'Bedrag'}, inplace = True)
data_ABN_34 = data[['Rekening','Datum','Bedrag', 'Categorie', 'Subcategorie', 'Land', 'Omschrijving']]

file2021 = '/home/marijke/Documents/Finances/Bankoverzichten/ABN_37_2021.ods'
file2022='/home/marijke/Documents/Finances/Bankoverzichten/ABN_37_2022.ods'
data = pd.concat([pd.read_excel(file2021), pd.read_excel(file2022)])
data.insert(0, 'Rekening', 'ABN_37')
data.rename(columns = {'Transactiedatum':'Datum', 'Transactiebedrag':'Bedrag'}, inplace = True)
data_ABN_37 = data[['Rekening','Datum','Bedrag', 'Categorie', 'Subcategorie', 'Land', 'Omschrijving']]

file2021 = '/home/marijke/Documents/Finances/Bankoverzichten/Rabo_52_2021.ods'
file2022='/home/marijke/Documents/Finances/Bankoverzichten/Rabo_52_2022.ods'
data = pd.concat([pd.read_excel(file2021), pd.read_excel(file2022)])
data.insert(0, 'Rekening', 'Rabo_52')
data.rename(columns = {'Omschrijving-1':'Omschrijving'}, inplace = True)
data_Rabo_52 = data[['Rekening','Datum','Bedrag', 'Categorie', 'Subcategorie', 'Land', 'Omschrijving']]


file2021 = '/home/marijke/Documents/Finances/Bankoverzichten/Rabo_64_2021.ods'
file2022='/home/marijke/Documents/Finances/Bankoverzichten/Rabo_64_2022.ods'
data = pd.concat([pd.read_excel(file2021), pd.read_excel(file2022)])
data.insert(0, 'Rekening', 'Rabo_64')
data.rename(columns = {'Omschrijving-1':'Omschrijving'}, inplace = True)
data_Rabo_64 = data[['Rekening','Datum','Bedrag', 'Categorie', 'Subcategorie', 'Land', 'Omschrijving']]

file2021 = '/home/marijke/Documents/Finances/Bankoverzichten/Rabo_CC_2021.ods'
file2022='/home/marijke/Documents/Finances/Bankoverzichten/Rabo_CC_2022.ods'
data = pd.concat([pd.read_excel(file2021), pd.read_excel(file2022)])
data.insert(0, 'Rekening', 'Rabo_CC')
data_Rabo_CC = data[['Rekening','Datum','Bedrag', 'Categorie', 'Subcategorie', 'Land', 'Omschrijving']]

data = pd.concat([data_ABN_34, data_ABN_37, data_Rabo_52, data_Rabo_64, data_Rabo_CC])

#Land NaN
# Goede lengte dataframes


Categories = data['Categorie'].unique()
Categories.sort()

for name in Categories:
    subdata = data[data['Categorie'] == name]
    Subcategories = subdata['Subcategorie'].unique()
    Subcategories.sort()
    print(name + ": ", str(Subcategories), '\n')

#print(data[data["Categorie"].str.contains("Verzekeringen", na = False)])
