import datetime
import json
with open("User.json",'r')as file:
    data=json.load(file)
if(len(data)!=0):
    id=data[len(data)-1]['id']
    name=data[len(data)-1]['name']
    Bal=data[len(data)-1]['transaction']['balance']
    print(id)
    print(name)
else:
    name=input("ENTER YOUR NAME")
    Bal=int(input("ENTER YOUR BALANCE"))
    id=-1
def BalanceAdd_enquiry(Bal,val,id):    
    data.append({"id":id,"name":name,"transaction":{
        "income":val,
        "balance":Bal,
        "date":str(datetime.datetime.now()),
        "note":note
    }})
    return data

def Expense_enquiry(Bal,expense,id):
    note=input("enter the note")
    data.append({"id":id,"name":name,"transaction":{
            "expense":expense,"balance":Bal,
            "date":str(datetime.datetime.now()),
            "note":note
        }})
    return data
    

while(True):
    choice=int(input("Enter 1 for add Income Enter 2 for Expence Enter 3 for exit "))
    if(choice==1):
        id+=1
        val=int(input("Enter the Income to add"))
        note=input("Enter purpose")
        Bal+=val
        data=BalanceAdd_enquiry(Bal,val,id)
    elif(choice==2):
        print(Bal)
        expense=int(input("Enter the Expense to add"))
        if(expense<Bal):
            id+=1
            Bal-=expense
            data=Expense_enquiry(Bal,expense,id)
        else:
            print("--:Expense Exceeds  your Balance:-- ")
    
    else:
        break
    print(data)
with open('User.json','w') as json_file:
    json.dump(data, json_file, indent=4)

"""dict structure
{id:some id, name:"given name",transaction:{
"Income":bal+val:
date:datetime of transaction,
note:"reason" 
}
{
}}
"""
