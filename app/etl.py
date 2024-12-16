import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from datetime import datetime

DATABASE_URI = "postgresql+psycopg2://username:password@localhost/dbname"
engine = create_engine(DATABASE_URI)

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def validate_and_clean_data(df):
    cleaned_data = []
    for _, row in df.iterrows():
        try:
            user_id = int(row['user_id'])
            name = row['name'].strip()
            email = row['email'].strip().lower()
            domain = email.split('@')[1]
            signup_date = datetime.strptime(row['signup_date'], '%Y-%m-%d').date()

            cleaned_data.append({
                "user_id": user_id,
                "name": name,
                "email": email,
                "domain": domain,
                "signup_date": signup_date
            })
        except (ValueError, KeyError) as e:
            print(f"Error validating row {row}: {e}")
            continue
    return cleaned_data


def insert_into_db(data, engine):
    with engine.begin() as connection:
        for record in data:
            try:
                connection.execute(
                    """
                    INSERT INTO users (user_id, name, email, domain, signup_date)
                    VALUES (%(user_id)s, %(name)s, %(email)s, %(domain)s, %(signup_date)s)
                    ON CONFLICT (user_id) DO NOTHING;
                    """,
                    record
                )
            except IntegrityError as e:
                print(f"Database integrity error: {e}")
            except Exception as e:
                print(f"Error inserting record {record}: {e}")

def main():
    csv_path = "users_data_with_errors.csv"
    df = load_csv(csv_path)

    if df is not None:
        print("CSV loaded successfully.")
        cleaned_data = validate_and_clean_data(df)
        print(f"Cleaned {len(cleaned_data)} records out of {len(df)} total.")
        insert_into_db(cleaned_data, engine)
        print("ETL process completed.")
    else:
        print("ETL process failed due to CSV loading issue.")

if __name__ == "__main__":
    main()