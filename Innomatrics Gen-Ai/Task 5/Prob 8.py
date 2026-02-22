# 8) Banking – Daily Transaction Limit Checker
def check_transaction_limit(transaction_amount):
    daily_limit = 50000
    if transaction_amount <= daily_limit:
        status = "Approved"
    else:
        status = "Rejected"
    print(f"Transaction Amount: {transaction_amount}")
    print(f"Transaction Status: {status}")

print("Scenario 1: Approved Transaction")
check_transaction_limit(45000)
print();
print("Scenario 2: Rejected Transaction")
check_transaction_limit(60000)
print();
print("Scenario 3: Borderline Approved Transaction")
check_transaction_limit(50000)