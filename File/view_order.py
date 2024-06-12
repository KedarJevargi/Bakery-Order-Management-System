import pandas as pd
class View_Orders:
    def __init__(self): 
        pass
        
    def view(self):

        # Read an Excel file
        df=pd.read_excel('main_data.xlsx',sheet_name='First Sheet')

        with open("dat.txt") as d:
            s=int(d.read())
        for i in range(s):
            if(df.at[i,"Status"]=="Processing"):
                print(f"Order ID: {df.at[i,'Order ID']}") 
                print(f"Cake Flavour: {df.at[i,'Flavour']}") 
                print(f"Cake Shape: {df.at[i,'Shape']}") 
                print(f"Cake Weight: {df.at[i,'Weight']}") 
                print(f"Egg/Eggless: {df.at[i,'Egg/Eggless']}") 
                print("--------------------------------------------------")

