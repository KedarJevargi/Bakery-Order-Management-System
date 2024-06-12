import pandas as pd
class Order_Status:
    def _init_(self):
        pass
    def check(self):
        a=input("Enter your Order ID\n")
        d=int(a[0])-1
        type(d)
        
        # Read an Excel file
        df=pd.read_excel('main_data.xlsx',sheet_name='First Sheet')

        # View the value of a specific cell
        cell_value = df.at[d,"Status"]
        print(cell_value)