import pandas as pd
import openpyxl

# sheet_name start at 0

path = 'STMASR02.xlsx'

colnames = ['raw','description','unit']
df = pd.read_excel(path, sheet_name=0, usecols="F,J,K", skiprows=5, names = colnames, engine = 'openpyxl')

#test = df.query('raw.astype(str).str.len() == 13',engine='python')

mask = (df["raw"].astype(str).str.len() == 13)
pre_barcode_df = df.loc[mask]

mask = (df["raw"].astype(str).str.len() != 13)
pre_sku_df = df.loc[mask]

# print(pre_sku_df)


barcode = []
for index, row in df.iterrows():

  #  print("in:",row["raw"])
    if len(str(row["raw"])) == 13:
        newdata = row["raw"]
    if len(str(row["raw"])) != 13:
  #      print(row["description"])
        mydes = row["description"]
        #print("=2=",pre_barcode_df.query("description == @mydes")["raw"])
        newrow = pre_barcode_df[pre_barcode_df["description"]==mydes]["raw"].tolist()
        #print(">",len(newrow))
        if len(newrow):
            newdata = str(newrow)[1:-1]
        else:
            newdata = "not found"

    barcode.append(newdata)
    #print("out:",newdata)
  


#print(barcode[:20])

with open(r'barcode.txt', 'w') as fp:
    fp.write("barcode\n")
    for item in barcode:
        # write each item on a new line
        fp.write("%s\n" % item)
    
