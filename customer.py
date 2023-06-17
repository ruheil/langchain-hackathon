import pandas as pd
from prettytable import PrettyTable

def getCustomerData(by, searchString):
    """Get customer data from customers.csv file.
    
    Keyword arguments:
    by -- 'name' or 'id'
    searchString -- the name or id of the customer
    """
    
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
    """ View all customers data from customers.csv file.
    
    Keyword arguments:
    None
    """
    
    df = pd.read_csv('customers.csv')
    table = PrettyTable()
    table.field_names = df.columns
    for _, row in df.iterrows():
        table.add_row(row)
    return table


def createCustomer(id, name, email, isActive, created):
    """ Create a new customer and save it to customers.csv file.
    
    Keyword arguments:
    id -- the id of the customer
    name -- the name of the customer
    email -- the email of the customer
    isActive -- whether the customer is active or not
    created -- the date the customer was created
    """
    new_customer = pd.DataFrame([[id, name, email, isActive, created]], columns=['id', 'name', 'email', 'isActive', 'created'])
    df = pd.read_csv('customers.csv')
    df = pd.concat([df, new_customer], ignore_index=True)
    df.to_csv('customers.csv', index=False)
    return "Customer created successfully."


# Sample usage
#createCustomer(1001, 'John Doe', 'johndoe@example.com', True, '2023-06-15')
#createCustomer(1002, 'Jane Smith', 'janesmith@example.com', False, '2023-06-16')

#customer = getCustomerData('id', '1001')
#print(customer)

#viewCustomersData()
