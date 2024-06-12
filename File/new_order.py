import pandas as pd
class New_Order:
    def _init_(self):
        pass
    def info(self):
        name=input("Enter your name\n")
        phone_no=input("Enter your phone number\n")
        items={"Flavour":{"1":"Honey Cake","2":"Red Velvet","3":"Death By Chocolate","4":"Black Forest","5":"Pineapple"},"Shape":{"1":"Circle","2":"Heart","3":"Square"},"Weight":{"1":"250g","2":"500g","3":"1000g"},"Egg":{"1":"Egg","0":"Eggless"}}
        price={"1":{"250g":200,"500g":400,"1000g":800},"0":{"250g":250,"500g":450,"1000g":850}}
        print("Enter the numbers for the respective options\n")
        flavour=input("Flavour:\n")
        shape=input("Shape:\n")
        weight=input("Weight:\n")
        eggless=input("Egg/Eggless cake:\n")
        adv_amount=input("Enter the advance amount:\n")
        rem_amount=int(price[eggless][items["Weight"][weight]])-int(adv_amount)
        print(f"Balance Amount: {rem_amount}\n")

        with open("dat.txt") as d:
            a=d.read()
            s=int(a)+1
        with open("dat.txt",mode="w") as d:
            d.write(str(s))

        
        order_id=str(s)+"_"+phone_no[0:5] 
        print(f"Here's the order ID : {order_id}\n")   

        # Read an Excel file
        df=pd.read_excel('main_data.xlsx', sheet_name='First Sheet')

        # Update the value of a specific cell
        df.at[s,'Order ID'] = order_id
        df.at[s,'Customer Name'] = name
        df.at[s,'Contact No'] =phone_no
        df.at[s,'Flavour'] = items["Flavour"][flavour]
        df.at[s,'Shape'] = items["Shape"][shape]
        df.at[s,'Weight'] = items["Weight"][weight]
        df.at[s,'Egg/Eggless'] = items["Egg"][eggless]
        df.at[s,'Total Amount'] = price[eggless][items["Weight"][weight]]
        df.at[s,'Advance Amount'] = adv_amount
        df.at[s,'Remaining Amount'] = rem_amount
        df.at[s,'Status']="Processing"

        # Save the changes back to the Excel file
        df.to_excel('main_data.xlsx', sheet_name='First Sheet',index=False)