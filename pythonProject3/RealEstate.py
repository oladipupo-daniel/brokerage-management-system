import re
class Customer:
    def __init__(self, custName, contactNo, flatType, amount, brokerageAmount):
        self.custName = custName
        self.contactNo = contactNo
        self.flatType = flatType
        self.amount = amount
        self.brokerageAmount = brokerageAmount

custList =[]

while True:
    print("...................ABC REAL ESTATE..................")
    print("1. Add New Customer")
    print("2. View All Customer")
    print("3. Calculate Brokerage Amount")
    print("4. Exit the Application")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        custName = input("Enter Customer Name: ")
        if re.match("^[A-Za-z]+$", custName):
            contactNo = input("Enter Contact Number: ")
            if re.match(r"^0(70|80|81|90|91)\d{8}$", contactNo):
                flatType = (input("Enter flat Type in BHK: "))
                if re.match("^[1-4]$", flatType):
                    amount = float(input("Enter Amount : "))
                    if flatType == '1':
                        brokerageAmount = amount*7/100
                    elif flatType == '2':
                        brokerageAmount = amount*10/100
                    elif flatType == '3':
                        brokerageAmount = amount*12/100
                    elif flatType == '4':
                        brokerageAmount = amount*15/100
                    custList.append(Customer(custName, contactNo, flatType, amount, brokerageAmount))
                    print("customer added successfully")
                else:
                    print("flat Type should be between 1-4")
            else:
                print("Enter 11 Digit Mobile Number: ")

        else:
            print("Please Input Valid Name:")

    elif ch == 2:
       print("CustName\tContact No\tFlat\tAmount\tBrokerage")
       for obj in custList:
           print(obj.custName,"\t",obj.contactNo,"\t",obj.flatType,"\t",obj.amount,"\t",obj.brokerageAmount)

    elif ch == 3:
       total = 0
       for obj in custList:
           total = total + obj.brokerageAmount
       print("Total Brokerage Amount Received is: ",total)
    elif ch == 4:
       print("Are you sure you want to quit Application: ")
       opt = input("Yes or No: ")
       if opt == "YES" or opt == "yes" or opt == "Yes":
           print("Thank You!")
           exit(1)
       else:
           continue
    else:
       print("Enter Valid Choice")
