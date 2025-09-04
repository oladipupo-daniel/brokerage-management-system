from utils.db import get_connection  # or from Brokerage.utils.db if you're using package imports

class Customer:
    def __init__(self, custName, contactNo, flatType, amount, brokerageAmount):
        self.custName = custName
        self.contactNo = contactNo
        self.flatType = flatType
        self.amount = amount
        self.brokerageAmount = brokerageAmount

    def save_to_db(self):
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO customers (name, contact, flat_type, amount, brokerage)
                    VALUES (%s, %s, %s, %s, %s)
                """, (self.custName, self.contactNo, self.flatType, self.amount, self.brokerageAmount))
                conn.commit()
                cursor.close()
                conn.close()
                print("✅ Customer saved to database.")
            except Exception as e:
                print(f"❌ Failed to save customer: {e}")
        else:
            print("❌ Could not connect to database. Customer not saved.")


