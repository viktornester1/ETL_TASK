import pandas as pd
import random
import faker
from datetime import datetime

fake = faker.Faker()
domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com", "company.org"]
data_with_errors = []
user_ids = set()

for _ in range(1000):
    while True:
        user_id = random.randint(1000, 9999)
        if user_id not in user_ids:
            user_ids.add(user_id)
            break

    name = fake.name()

    # (5% chance of error)
    is_valid_email = random.random() < 0.95
    if is_valid_email:
        email = f"{fake.user_name()}@{random.choice(domains)}"
    else:
        error_type = random.choice(["no_at", "at_end", "at_beginning"])
        if error_type == "no_at":
            email = f"{fake.user_name()}example.com"
        elif error_type == "at_end":
            email = f"{fake.user_name()}@"
        else:  # at_beginning
            email = f"@{fake.user_name()}"

    signup_date = fake.date_this_decade(before_today=True, after_today=False)
    signup_time = fake.time()
    signup_date = f"{signup_date}T{signup_time}"

    data_with_errors.append([user_id, name, email, signup_date])

df_with_errors = pd.DataFrame(data_with_errors, columns=["user_id", "name", "email", "signup_date"])

csv_file_path_with_errors = r"/ETL_Task/data/users_data_with_errors.csv"
df_with_errors.to_csv(csv_file_path_with_errors, index=False)
