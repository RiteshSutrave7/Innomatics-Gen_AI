# 6: Duplicate User ID Detection
user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]
# dictionary to store the count of each user id
counts={}
# Identify duplicate user IDs.
for user_id in user_ids:
    counts[user_id]=counts.get(user_id,0)+1
# Display how many times each duplicate appears.
for user_id,count in counts.items():
    if count>1:
        print(f"{user_id}->{count}times")