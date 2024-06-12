import pandas as pd
import os
from new_order import New_Order
from order_status import Order_Status
from update_status import Update_Status
from view_order import View_Orders
from print_bill import Print_Bill

with open("dat.txt") as d:
    if int(d.read())==0:
        # Create a DataFrame
        data = {    
            'Order ID': [],
            'Customer Name': [],
            'Contact No': [],
            'Flavour': [],
            'Shape': [],
            'Weight': [],
            'Egg/Eggless': [],
            'Total Amount': [],
            'Advance Amount': [],
            'Remaining Amount': [],
            'Status':[]
        }
        df = pd.DataFrame(data)
        # Write the DataFrame to a new Excel file
        df.to_excel('main_data.xlsx', sheet_name='First Sheet', index=False)

def display_menu():
    menu = """
    ======================================
                  MAIN MENU
    ======================================
    1. New Order
    2. Check Status
    3. View Orders
    4. Update Order Status
    5. Print Bill
    ======================================
    Please select an option (1-5):
    """
    return input(menu)

choice = display_menu()

if choice=="1":
    os.system('clear')
    
    from PIL import Image 
    im = Image.open("baker_reference.jpg") 
    im.show()

    c=New_Order()
    c.info()

elif choice=="2":
    os.system('clear')
    m=Order_Status()
    m.check()

elif choice=="3":
    os.system('clear')
    v=View_Orders()  
    v.view()
    
elif choice=="4":
    os.system('clear')
    n=Update_Status()
    n.update()
    
else:
    os.system('clear')
    x=Print_Bill()
    x.print()    



