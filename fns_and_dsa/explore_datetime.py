from datetime import datetime,timedelta

def display_current_datetime():
    current_date= datetime.datetime.now()
    print("Current date and time:", current_date.strftime('%Y %m %d %H:%M:%S'))


def calculate_future_date():
    future_date = int(input('Enter the number of days to add to the current date: '))

if __name__ == '__main__':
    display_current_datetime()
    calculate_future_date()