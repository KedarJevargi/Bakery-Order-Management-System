import pandas as pd
class Update_Status:
    def __init__(self): 
        pass
    def update(self):

        # Read an Excel file
        df = pd.read_excel('main_data.xlsx', sheet_name='First Sheet')

        a=input("Enter your Order ID\n")
        d=int(a[0])-1
        type(d)
        
        # Update the value of a specific cell
        df.at[d,"Status"] ="Ready for delivery"

        # Save the changes back to the Excel file
        df.to_excel('main_data.xlsx', sheet_name='First Sheet', index=False)

        print(f"The Order ID {a} has been updated")

