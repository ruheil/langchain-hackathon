import pandas as pd
from prettytable import PrettyTable

def getCustomerData(by, searchString):
    df = pd.read_csv('customers.csv')
    if by == 'name':
        result = df[df['name'].str.contains(searchString, case=False)]
    elif by == 'id':
        result = df[df['id'] == int(searchString)]
    else:
        return "Invalid 'by' argument. It should be either 'name' or 'id'."

    if result.empty:
        return "No customer found."
    else:
        return result.to_dict(orient='records')[0]


def viewCustomersData():
    df = pd.read_csv('customers.csv')
    table = PrettyTable()
    table.field_names = df.columns
    for _, row in df.iterrows():
        table.add_row(row)
    print(table)


def createCustomer(id, name, email, isActive, created):
    new_customer = pd.DataFrame([[id, name, email, isActive, created]], columns=['id', 'name', 'email', 'isActive', 'created'])
    df = pd.read_csv('customers.csv')
    df = pd.concat([df, new_customer], ignore_index=True)
    df.to_csv('customers.csv', index=False)
    print("New customer created successfully.")


# Sample usage
#createCustomer(1001, 'John Doe', 'johndoe@example.com', True, '2023-06-15')
#createCustomer(1002, 'Jane Smith', 'janesmith@example.com', False, '2023-06-16')

#customer = getCustomerData('id', '1001')
#print(customer)

#viewCustomersData()
