from Brokerage.client import Customer
from Brokerage.utils.helpers import (
    validate_name, validate_contact, validate_flat_type, calculate_brokerage
)
from Brokerage.transaction import execute_transaction
from Brokerage.portfolio import display_portfolio

custList = []

def main():
    while True:
        print("\n...................ABC REAL ESTATE..................")
        print("1. Add New Customer")
        print("2. View All Customers")
        print("3. Calculate Total Brokerage")
        print("4. Execute Transaction")
        print("5. View Portfolio")
        print("6. Exit")

        try:
            ch = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == 1:
            custName = input("Enter Customer Name: ")
            if not validate_name(custName):
                print("Please input a valid name.")
                continue

            contactNo = input("Enter Contact Number: ")
            if not validate_contact(contactNo):
                print("Enter a valid 11-digit mobile number.")
                continue

            flatType = input("Enter Flat Type in BHK (1-4): ")
            if not validate_flat_type(flatType):
                print("Flat Type should be between 1-4.")
                continue

            try:
                amount = float(input("Enter Amount: "))
            except ValueError:
                print("Amount must be a number.")
                continue

            brokerageAmount = calculate_brokerage(flatType, amount)
            custList.append(Customer(custName, contactNo, flatType, amount, brokerageAmount))
            print("Customer added successfully.")

        elif ch == 2:
            print("\nCustName\tContact No\tFlat\tAmount\tBrokerage")
            for obj in custList:
                print(f"{obj.custName}\t{obj.contactNo}\t{obj.flatType}\t{obj.amount}\t{obj.brokerageAmount}")

        elif ch == 3:
            total = sum(obj.brokerageAmount for obj in custList)
            print("Total Brokerage Amount Received is:", total)

        elif ch == 4:
            name = input("Enter customer name: ")
            asset = input("Enter asset name: ")
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Quantity must be a number.")
                continue
            action = input("Buy or Sell: ").lower()

            for client in custList:
                if client.custName == name:
                    execute_transaction(client, asset, quantity, action)
                    break
            else:
                print("Client not found.")

        elif ch == 5:
            name = input("Enter customer name: ")
            for client in custList:
                if client.custName == name:
                    display_portfolio(client)
                    break
            else:
                print("Client not found.")

        elif ch == 6:
            opt = input("Are you sure you want to quit? (Yes/No): ")
            if opt.lower() == "yes":
                print("Thank you for using ABC Real Estate!")
                break
        else:
            print("Enter a valid choice.")

if __name__ == "__main__":
    main()
