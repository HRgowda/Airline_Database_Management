import mysql.connector
import sys

def get_connection():
    conn = mysql.connector.connect(
        host='localhost', port=3306,
        user='root',
        password='Hemanth18$#@',
        db='airline_data', charset='utf8'
    )
    return conn

def insert():
    Airline_name = input("Enter the airline name: ")
    country = input("Enter the country name: ")
    Aircraft_id = input("Enter aircraft id: ")
    model = input("Enter the model: ")
    capacity = int(input("Enter capacity: "))
    status = input("Enter flight status (Active/Maintenence): ")
    conn = get_connection()
    my_cursor = conn.cursor()
    insert_query = """insert into Airline(Airline_name, Country, Aircraft_ID, Model, Capacity, Flight_Status) values (%s, %s, %s, %s, %s, %s )"""
    record = (Airline_name, country, Aircraft_id, model, capacity, status)
    my_cursor.execute(insert_query, record)
    conn.commit()
    my_cursor.close()
    conn.close()
    return "Successfully inserted a row!"

def search():
    airline_id = int(input("Enter airline id to search: "))
    conn = get_connection()
    search_query = """select * from Airline where Airline_ID = %s"""
    my_cursor = conn.cursor()
    my_cursor.execute(search_query, (airline_id,))
    row_data = my_cursor.fetchone()
    if row_data is None:
        return "Aircraft with ID:{} not found".format(airline_id)
    print(f"Aircraft details are: ")
    print(str(row_data))
    return '\n Aircraft with ID: {} details displayed successfully'.format(airline_id)

def print_records(rows):
    # Define headers and rows
    headers = ['Airline_id', 'Airline_name', 'Country', 'Aircraft_ID', 'Model', 'Capacity', 'Flight_Status']

    # Calculate maximum width for each column
    max_widths = [max(len(str(item)) for item in column) for column in zip(headers, *rows)]

    # Print headers with proper spacing
    print(' '.join(f'{header:<{width}}' for header, width in zip(headers, max_widths)))

    # Print rows with proper spacing
    for row in rows:
        formatted_row = [str(item).ljust(width) for item, width in zip(row, max_widths)]
        print(' '.join(formatted_row))

# Example usage:
rows = [
    ('1', 'Airline1', 'Country1', 'A123', 'Model1', 200, 'On-time'),
    ('2', 'Airline2', 'Country2', 'B456', 'Model2', 150, 'Delayed')
]



def list_all():
    conn = get_connection()
    my_cursor = conn.cursor()
    sql_query = 'select * from Airline'
    my_cursor.execute(sql_query)
    table_data = my_cursor.fetchall()
    if not table_data:
        return 'No rows available in the table'
    my_cursor.close()
    conn.close()

    print_records(table_data)
    return 'All records fetched and printed successfully'

def update_one():
    airline_id = input('Enter ID of the airline to update the record : ')
    new_name = input('Enter the new airline name to be updated : ')
    model = input('Enter the new model name of the aircraft : ')
    country = input("Enter the country to update: ")
    status = input("Enter the flight status: ")
    my_connection = get_connection()
    my_cursor = my_connection.cursor()
    update_query = """update Airline set Airline_name=%s, Model=%s, Country=%s, Flight_Status=%s where Airline_ID=%s"""
    new_airline_data = (new_name, model, country, status, airline_id)
    my_cursor.execute(update_query, new_airline_data)
    my_connection.commit()
    my_cursor.close()
    my_connection.close()
    if my_cursor.rowcount == 1:
        return 'Record updated and saved successfully'
    else:
        return 'Record with ID: {} not found'.format(airline_id)

def delete_one():
    airline_id = input('Enter airline ID to delete the record: ')
    my_connection = get_connection()
    my_cursor = my_connection.cursor()
    delete_query = """delete from Airline where Airline_ID=%s"""
    my_cursor.execute(delete_query, airline_id)
    my_connection.commit()
    check_query = """select * from Airline where Airline_ID=%s"""
    my_cursor.execute(check_query, airline_id)
    deleted_record = my_cursor.fetchone()
    my_cursor.close()
    my_connection.close()
    if deleted_record is None:
        return 'Record with ID:{} deleted successfully'.format(airline_id)
    else:
        return 'Record with ID: {} not found'.format(airline_id)


def exit_program():
    sys.exit('End of program')

def invalid_choice():
    return 'Invalid choice entered'

def start_app():
    crud_options = {
        1 : insert,
        2 : search,
        3 : list_all,
        4 : update_one,
        5 : delete_one,
        6 : exit_program
    }
    count_of_operations = 20
    while count_of_operations >= 1:
        print('1:Insert 2:Search 3:Display 4:Update 5:Delete 6:Exit')
        choice = int(input('Your choice please: '))
        print(crud_options.get(choice, invalid_choice)() )
        count_of_operations -= 1
    print('End of program') 

#Main Code
start_app()
