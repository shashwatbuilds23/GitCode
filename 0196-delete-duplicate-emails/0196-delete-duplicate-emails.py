import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 1. Sort by id to ensure the smallest id is evaluated first
    person.sort_values(by='id', ascending=True, inplace=True)
    
    # 2. Drop duplicates based on email, keeping the first (smallest id)
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    