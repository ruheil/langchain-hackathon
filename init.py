import pandas as pd

def createInitialCSV():
    data = {
        'id': [],
        'name': [],
        'email': [],
        'isActive': [],
        'created': []
    }
    df = pd.DataFrame(data)
    df.to_csv('customers.csv', index=False)
    print("Initial CSV created successfully.")

# Create the initial CSV file
createInitialCSV()