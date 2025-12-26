fees = {}

def pay_fee(roll, amount):
    fees[roll] = amount

def get_fee_status(roll):
    return fees.get(roll, 0)
