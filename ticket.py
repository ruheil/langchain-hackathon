import csv
from prettytable import PrettyTable

def openTicket(customerID, customerName, complain, timestamp):
    ticket_data = [customerID, customerName, complain, timestamp]

    with open('tickets.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ticket_data)

def viewTickets():
    with open('tickets.csv', 'r') as file:
        reader = csv.reader(file)
        tickets = list(reader)

        if len(tickets) == 0:
            print("No tickets found.")
        else:
            headers = ['Customer ID', 'Customer Name', 'Complain', 'Timestamp']
            table = PrettyTable(headers)
            table.align = 'l'

            for ticket in tickets:
                table.add_row(ticket)

            print(table)

# Example usage
#openTicket(1, "John Doe", "Slow internet speed", "2023-06-16 10:00:00")
#openTicket(2, "Jane Smith", "No electricity", "2023-06-16 14:30:00")
#viewTickets()
