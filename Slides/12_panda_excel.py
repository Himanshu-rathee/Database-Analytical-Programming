import pandas as pd
excel = pd.ExcelFile("Financial Sample.xlsx")
print(excel.sheet_names)

df = excel.parse(excel.sheet_names[0])
#print(df)

df1 = excel.parse(0)
#print(df1.head(7))


print(df1.loc[5,["Segment", "Profit", "Date"]])