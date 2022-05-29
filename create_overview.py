import pandas as pd
import numpy as np

data = pd.read_pickle("/home/marijke/Documents/Finances/Bankoverzichten/uitgaven.pkl")

print(data[data["Subcategorie"] == "Inboedel"])

widths = [25,10,7]
str_bet = '     |'


month_2021 = ['01', '02','03','04','05','06','07','08','09','10','11','12']
month_2021 = reversed(month_2021)
month_2022 =['01', '02','03','04']
month_2022 = reversed(month_2022)
Categories = data['Categorie'].unique()
Categories.sort()
with open('/home/marijke/Documents/Finances/Bankoverzichten/table.txt', 'w') as f:
    f.write(f"{'|':>{widths[0]}}")
    f.write(f"{'TOT 16mn|':>{widths[1]}}")
    f.write(f"{'AVG 16mn|':>{widths[1]}}")
    f.write(f"{'TOT 2022|':>{widths[1]}}")
    f.write(f"{'AVG 2022|':>{widths[1]}}")
    f.write(f"{'TOT 2021|':>{widths[1]}}")
    f.write(f"{'AVG 2021|':>{widths[1]}}")



    f.write(str_bet)
    for month in month_2022:
        f.write(f"{'22-' + month + '|':>{widths[2]}}" )
    for month in month_2021:
        f.write(f"{'21-' + month + '|':>{widths[2]}}")
    f.write("\n")
    for name in Categories:
        subdata = data[data['Categorie'] == name]
        Subcategories = subdata['Subcategorie'].unique()
        Subcategories.sort()
        f.write('-' * 200 + '\n')
        f.write(f"{name:<{widths[0]-1}}")
        f.write('|')



        total_cat = data[data["Categorie"] == name]
        total_cat_sum = -1 *  round(total_cat["Bedrag"].sum())
        # Tot 16
        f.write(f"{total_cat_sum :>{widths[1]-1}}")
        f.write('|')
        # AVG 16
        f.write(f"{round(total_cat_sum /16):>{widths[1]-1}}")
        f.write('|')

        # TOT 2022
        data_2022 = data[data['Datum'].astype(str).str.contains("2022")]
        total_2022_cat = data_2022[data["Categorie"] == name]
        total_2022_cat_sum = -1 *  round(total_2022_cat["Bedrag"].sum())
        f.write(f"{total_2022_cat_sum :>{widths[1]-1}}")
        f.write('|')
        # AVG 2022
        f.write(f"{round(total_2022_cat_sum /4):>{widths[1]-1}}")
        f.write('|')

        data_2021 = data[data['Datum'].astype(str).str.contains("2021")]
        total_2021_cat = data_2021[data["Categorie"] == name]
        total_2021_cat_sum = -1 *  round(total_2021_cat["Bedrag"].sum())
        f.write(f"{total_2021_cat_sum :>{widths[1]-1}}")
        f.write('|')
        # AVG 2021
        f.write(f"{round(total_2021_cat_sum /4):>{widths[1]-1}}")
        f.write('|')

        #month
        f.write(str_bet)
        month_2021 = ['01', '02','03','04','05','06','07','08','09','10','11','12']
        month_2021 = reversed(month_2021)
        month_2022 =['01', '02','03','04']
        month_2022 = reversed(month_2022)
        for month in month_2022:
            total_2022_cat_month = total_2022_cat[total_2022_cat['Datum'].astype(str).str.contains(month)]
            total_2022_cat_sum = -1 *  round(total_2022_cat_month["Bedrag"].sum())
            f.write(f"{total_2022_cat_sum:>{widths[2]}}" )
        for month in month_2021:
            total_2021_cat_month = total_2021_cat[total_2021_cat['Datum'].astype(str).str.contains(month)]
            total_2021_cat_sum = -1 *  round(total_2021_cat_month["Bedrag"].sum())
            f.write(f"{total_2021_cat_sum:>{widths[2]}}" )

        # TOT 2021


        # AVG 2021





        f.write('\n' + '-' * 200 + '\n')

        for subname in Subcategories:

            total_subcat = total_cat[total_cat["Subcategorie"] == subname]
            total_subcat_sum = -1 *  round(total_subcat["Bedrag"].sum())
            f.write(f"{subname:>{widths[0]-1}}")
            f.write('|')
            f.write(f"{total_subcat_sum :>{widths[1]-1}}")
            f.write('|')
            # AVG 16
            f.write(f"{round(total_subcat_sum /16):>{widths[1]-1}}")
            f.write('|')


            total_2022_subcat = total_2022_cat[total_2022_cat["Subcategorie"] == subname]
            total_2022_subcat_sum = -1 *  round(total_2022_subcat["Bedrag"].sum())
            f.write(f"{total_2022_subcat_sum :>{widths[1]-1}}")
            f.write('|')
            # AVG 2021
            f.write(f"{round(total_2022_subcat_sum /4):>{widths[1]-1}}")
            f.write('|')

            total_2021_subcat = total_2021_cat[total_2021_cat["Subcategorie"] == subname]
            total_2021_subcat_sum = -1 *  round(total_2021_subcat["Bedrag"].sum())
            f.write(f"{total_2021_subcat_sum :>{widths[1]-1}}")
            f.write('|')
            # AVG 2021
            f.write(f"{round(total_2021_subcat_sum /12):>{widths[1]-1}}")
            f.write('|')


            f.write(str_bet)
            month_2021 = ['01', '02','03','04','05','06','07','08','09','10','11','12']
            month_2021 = reversed(month_2021)
            month_2022 =['01', '02','03','04']
            month_2022 = reversed(month_2022)
            for month in month_2022:
                total_2022_subcat_month = total_2022_subcat[total_2022_subcat['Datum'].astype(str).str.contains(month)]
                total_2022_subcat_sum = -1 *  round(total_2022_subcat_month["Bedrag"].sum())
                f.write(f"{total_2022_subcat_sum:>{widths[2]}}" )
            for month in month_2021:
                total_2021_subcat_month = total_2021_subcat[total_2021_subcat['Datum'].astype(str).str.contains(month)]
                total_2021_subcat_sum = -1 *  round(total_2021_subcat_month["Bedrag"].sum())
                f.write(f"{total_2021_subcat_sum:>{widths[2]}}" )
            f.write('\n')



    f.write('-' * 200 + '\n')
    f.write('-' * 200 + '\n')


    f.write(f"{'TOTAAL':<{widths[0]-1}}")
    f.write('|')


    # TOTAAL
    total_sum = -1 *  round(data["Bedrag"].sum())
            # Tot 16
    f.write(f"{total_sum :>{widths[1]-1}}")
    f.write('|')
            # AVG 16
    f.write(f"{round(total_sum /16):>{widths[1]-1}}")
    f.write('|')

    # TOT 2022
    data_2022 = data[data['Datum'].astype(str).str.contains("2022")]
    total_2022_sum = -1 *  round(data_2022["Bedrag"].sum())
    f.write(f"{total_2022_sum :>{widths[1]-1}}")
    f.write('|')
            # AVG 2022
    f.write(f"{round(total_2022_sum /4):>{widths[1]-1}}")
    f.write('|')

    data_2021 = data[data['Datum'].astype(str).str.contains("2021")]
    total_2021_sum = -1 *  round(data_2021["Bedrag"].sum())
    f.write(f"{total_2021_sum :>{widths[1]-1}}")
    f.write('|')
    # AVG 2021
    f.write(f"{round(total_2021_sum /12):>{widths[1]-1}}")
    f.write('|')

    f.write(str_bet)
    month_2021 = ['01', '02','03','04','05','06','07','08','09','10','11','12']
    month_2021 = reversed(month_2021)
    month_2022 =['01', '02','03','04']
    month_2022 = reversed(month_2022)
    for month in month_2022:
        data_2022_month= data_2022[data_2022['Datum'].astype(str).str.contains(month)]
        total_2022_month_sum = -1 *  round(data_2022_month["Bedrag"].sum())
        f.write(f"{total_2022_month_sum:>{widths[2]}}" )
    for month in month_2021:
        data_2021_month= data_2021[data_2021['Datum'].astype(str).str.contains(month)]
        total_2021_month_sum = -1 *  round(data_2021_month["Bedrag"].sum())
        f.write(f"{total_2021_month_sum:>{widths[2]}}" )
    f.write('\n')


    f.write('-' * 200 + '\n')
