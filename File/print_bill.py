import pandas as pd
from openpyxl import load_workbook
import datetime 
class Print_Bill:
    def __init__(self): 
        pass
        
    def print(self):
        order_id=input("Enter the order ID\n")
        d=int(order_id[0])-1

        # Read an Excel file
        df = pd.read_excel('main_data.xlsx', sheet_name='First Sheet')
        
        # Load the workbook
        workbook = load_workbook('invoice worksheet.xlsx')

        # Select the worksheet
        worksheet = workbook['Invoice']  # Replace 'Sheet1' with your sheet name

        # Update the cell value
        worksheet['B1'] = "Order ID :"+ df.at[d,"Order ID"]
        worksheet['B7'] = df.at[d,"Customer Name"]
        worksheet['B8'] = df.at[d,"Contact No"]
        worksheet['B10'] = df.at[d,"Flavour"]
        worksheet['c10'] = df.at[d,"Total Amount"]
        worksheet['B5']=(f"Date: {datetime.date.today()}")
        
        # Update the value of a specific cell
        df.at[d,"Status"] ="Delivered"

        # Save the changes back to the Excel file
        df.to_excel('main_data.xlsx', sheet_name='First Sheet', index=False)

        # Save the workbook
        workbook.save("invoice worksheet.xlsx")
        print(f"The bill for order ID {order_id} has been printed")
        
