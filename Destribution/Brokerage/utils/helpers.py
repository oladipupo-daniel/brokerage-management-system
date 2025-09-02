import re

def validate_name(name):
    return re.match("^[A-Za-z]+$", name)

def validate_contact(contact):
    return re.match(r"^0(70|80|81|90|91)\d{8}$", contact)

def validate_flat_type(flat_type):
    return re.match("^[1-4]$", flat_type)

def calculate_brokerage(flat_type, amount):
    rates = {'1': 7, '2': 10, '3': 12, '4': 15}
    return amount * rates.get(flat_type, 0) / 100
