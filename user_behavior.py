import pandas as pd
import random

num_users = 20
user_data = []

for user_id in range(1, num_users + 1):
    viewed_products = random.sample(range(1, 71), random.randint(3, 8))
    for pid in viewed_products:
        action = random.choice(["viewed", "added_to_cart", "purchased"])
        rating = random.randint(1, 5)
        user_data.append([user_id, pid, action, rating])

df = pd.DataFrame(user_data, columns=["user_id", "product_id", "action", "rating"])
df.to_csv("data/user_behavior.csv", index=False)
print("✅ user_behavior.csv created with", len(df), "records")
