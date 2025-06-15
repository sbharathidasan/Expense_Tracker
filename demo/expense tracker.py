import datetime

name=input("ENTER YOUR NAME")

Bal=int(input("ENTER YOUR BALANCE"))
data=[]
id=0
def BalanceAdd_enquiry():    
    val=int(input("Enter the Income to add"))
    data.append({"id":id,"name":name,"transaction":{
        "income":Bal+val,
        "date":datetime.datetime
    }})
    
    print(data[0]["transaction"]["income"])
    print(data[0]["transaction"]["date"])
while(True):
    choice=int(input("Enter 1 for add Income Enter 2 for Expence Enter 3 for exit "))
    if(choice==1):
        BalanceAdd_enquiry()
    elif(choice==2):
        Expence_enquiry()
    else:
        break

"""dict structure
{id:some id, name:"given name",transaction:{
"Income":bal+val:
date:datetime of transaction,
note:"reason" 
}
{
}}
"""
