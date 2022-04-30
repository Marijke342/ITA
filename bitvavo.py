from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime
import pandas as pd

#f = open("/home/marijke/Documents/Finances/Excel Data/bitvavo.txt", "r")
#api_code = f.readlines()

with open("/home/marijke/Documents/Finances/Excel_Data/bitvavo.txt") as file:
    lines = file.read().splitlines()

bitvavo = Bitvavo({
  'APIKEY': lines[0],
  'APISECRET': lines[1],
  'RESTURL': 'https://api.bitvavo.com/v2',
  'WSURL': 'wss://ws.bitvavo.com/v2/',
  'ACCESSWINDOW': 10000,
  'DEBUGGING': False
})

response = bitvavo.depositHistory({})
for dict_item in response:
    dict_item["timestamp"] = datetime.fromtimestamp(dict_item["timestamp"]/1000.0)
df_deposits = pd.DataFrame.from_dict(response)
df_deposits_prep = df_deposits[['timestamp', 'amount', 'fee', 'address']]
df_deposits_prep=df_deposits_prep.rename(columns={"amount":"EUR"})



response = bitvavo.withdrawalHistory({})
for dict_item in response:
    dict_item["timestamp"] = datetime.fromtimestamp(dict_item["timestamp"]/1000.0)
df_withdrawal = pd.DataFrame.from_dict(response)
df_withdrawal["EUR"] = "0.0"
df_withdrawal["BTC"] = "0.0"
df_withdrawal["ETH"] = "0.0"
# go from object to float!
for index, row in df_withdrawal.iterrows():
    df_withdrawal.at[index,row["symbol"]]= -1 * row["amount"];
print(df_withdrawal)
df_withdrawal_prep = df_withdrawal[['timestamp', 'amount', 'fee', 'symbol', 'address']]
df_withdrawal["EUR"] = ""
df_withdrawal["BTC"] = ""
df_withdrawal["ETH"] = ""
df_withdrawal_prep=df_withdrawal_prep.rename(columns={"symbol":"fee-currency"})



response = bitvavo.trades('BTC-EUR', {})
for dict_item in response:
    dict_item["timestamp"] = datetime.fromtimestamp(dict_item["timestamp"]/1000.0)
df_tradesBTCEUR = pd.DataFrame.from_dict(response)

response = bitvavo.trades('ETH-EUR', {})
for dict_item in response:
    dict_item["timestamp"] = datetime.fromtimestamp(dict_item["timestamp"]/1000.0)
df_tradesETHEUR = pd.DataFrame.from_dict(response)


#print(df_deposits)
#print(df_withdrawal)
#print(df_tradesETHEUR)

#https://www.geeksforgeeks.org/merge-two-dataframes-with-same-column-names/


#df.to_excel('dict1.xlsx')
