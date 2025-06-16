import datetime
import json
name=input("ENTER YOUR NAME")

Bal=int(input("ENTER YOUR BALANCE"))
data=[]
id=0
def BalanceAdd_enquiry(Bal,val):    
    data.append({"id":id,"name":name,"transaction":{
        "income":val,
        "balance":Bal,
        "date":datetime.datetime,
        "note":note
    }})
    return data

def Expense_enquiry(Bal,expense):
    note=input("enter the note")
    data.append({"id":id,"name":name,"transaction":{
            "expense":expense,"balance":Bal,
            "date":datetime.datetime.now,
            "note":note
        }})
    return data
    

while(True):
    choice=int(input("Enter 1 for add Income Enter 2 for Expence Enter 3 for exit "))
    if(choice==1):
        val=int(input("Enter the Income to add"))
        note=input("Enter purpose")
        Bal+=val
        data=BalanceAdd_enquiry(Bal,val)
    elif(choice==2):
        print(Bal)
        expense=int(input("Enter the Expense to add"))
        if(expense<Bal):
            Bal-=expense
            data=Expense_enquiry(Bal,expense)
        else:
            print("--:Expense Exceeds  your Balance:-- ")
    
    else:
        break
    json_obj=json.dumps(data)
    print(json_obj)

"""dict structure
{id:some id, name:"given name",transaction:{
"Income":bal+val:
date:datetime of transaction,
note:"reason" 
}
{
}}
"""
