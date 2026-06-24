import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by email and count occurrences
    counts = person.groupby('email').size().reset_index(name='count')
    
    # Filter for counts > 1
    duplicated_emails = counts[counts['count'] > 1][['email']]
    
    # Rename column to match output format
    duplicated_emails.columns = ['Email']
    
    return duplicated_emails