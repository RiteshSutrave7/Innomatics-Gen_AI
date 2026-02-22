# 4) Social Media – Duplicate Account Detection 
def detect_duplicates(usernames):
    unique_users = set(usernames)

    if len(unique_users) != len(usernames):
        print("Duplicate Accounts Found: Yes")
    else:
        print("Duplicate Accounts Found: No")


users = ["john", "alice", "john", "mike"]
detect_duplicates(users)