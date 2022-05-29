import pandas as pd
import numpy as np

file2021 = '/home/marijke/Documents/Finances/Bankoverzichten/Pinnen_2021.ods'
file2022 = '/home/marijke/Documents/Finances/Bankoverzichten/Pinnen_2022.ods'
file_wisselkoers = '/home/marijke/Documents/Finances/Bankoverzichten/Wisselkoers.ods'

data_pin = pd.concat([pd.read_excel(file2021, sheet_name = 'Pinnen'), pd.read_excel(file2022, sheet_name = 'Pinnen')])
data_uitgaven = pd.concat([pd.read_excel(file2021, sheet_name = 'Uitgaven'), pd.read_excel(file2022, sheet_name = 'Uitgaven')])
data_wisselkoers = pd.read_excel(file_wisselkoers)

data_pin['Datum'] = data_pin['Datum'].astype(str).str[:-3]
data_uitgaven['Datum'] = data_uitgaven['Datum'].astype(str).str[:-3]
data_wisselkoers['Datum'] = data_wisselkoers['Datum'].astype(str).str[:-2]



month_2021 = ['01', '02','03','04','05','06','07','08','09','10','11','12']
month_2022 =['01', '02','03','04']

data_uitgaven_pinnen = pd.DataFrame()

for month in month_2021:

    print('\n', month)
    # Totaal gepind
    data_month_pin = data_pin[data_pin["Datum"] == '2021-'+month]
    total_pin_month = data_month_pin["Bedrag"].sum()


    # Wisselkeors
    wisselkoers = data_wisselkoers.loc[data_wisselkoers['Datum'] == '2021' + month, 'BRL'].iloc[0]

    # Totaal uitgegeven
    data_month_uitgaven = data_uitgaven[data_uitgaven["Datum"] == '2021-'+month]
    for ind in data_month_uitgaven.index:
        if np.isnan(data_month_uitgaven['Bedrag'][ind]):
            data_month_uitgaven['Bedrag'][ind] = -1 *  data_month_uitgaven['Bedrag Oorspronkelijk'][ind] / wisselkoers
            #a =1
            #row["Bedrag"] = data_wisselkoers['']
    onbekend_month = total_pin_month - data_month_uitgaven["Bedrag"].sum()
    row_onbekend = {'Datum': '2021-'+month, 'Bedrag' : onbekend_month, 'Beschrijving' : 'Onbekend via pin 2021 maand ' + month, 'Categorie':'Onbekend', 'Subcategorie': 'Pin onbekend'}
    data_month_uitgaven = data_month_uitgaven.append(row_onbekend, ignore_index = True)
    data_uitgaven_pinnen = data_uitgaven_pinnen.append(data_month_uitgaven, ignore_index = True)


for month in month_2022:

    #print('\n', month)
    # Totaal gepind
    data_month_pin = data_pin[data_pin["Datum"] == '2022-'+month]
    total_pin_month = data_month_pin["Bedrag"].sum()


    # Wisselkeors
    wisselkoers = data_wisselkoers.loc[data_wisselkoers['Datum'] == '2022' + month, 'BRL'].iloc[0]

    # Totaal uitgegeven
    data_month_uitgaven = data_uitgaven[data_uitgaven["Datum"] == '2022-'+month]
    for ind in data_month_uitgaven.index:
        if np.isnan(data_month_uitgaven['Bedrag'][ind]):
            data_month_uitgaven['Bedrag'][ind] = -1 *  data_month_uitgaven['Bedrag Oorspronkelijk'][ind] / wisselkoers
            #a =1
            #row["Bedrag"] = data_wisselkoers['']
    onbekend_month = total_pin_month - data_month_uitgaven["Bedrag"].sum()
    row_onbekend = {'Datum': '2022-'+month, 'Bedrag' : onbekend_month, 'Beschrijving' : 'Onbekend via pin 2022 maand ' + month, 'Categorie':'Onbekend', 'Subcategorie': 'Pin onbekend'}
    data_month_uitgaven = data_month_uitgaven.append(row_onbekend, ignore_index = True)
    print(data_month_uitgaven)
    data_uitgaven_pinnen = data_uitgaven_pinnen.append(data_month_uitgaven, ignore_index = True)

data_uitgaven_pinnen.insert(0, 'Rekening', 'Pinnen')
#rint(data_uitgaven_pinnen)
    #print(total_uitgaven_month)
