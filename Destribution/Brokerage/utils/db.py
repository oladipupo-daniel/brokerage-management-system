import pymysql

def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="broker_user",
            password="securepass123",
            database="brokerage_db"
        )
        print("✅ Connection established.")
        return conn
    except pymysql.MySQLError as err:
        print(f"❌ Connection failed: {err}")
        return None





