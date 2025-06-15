from datetime import datetime,timedelta

def display_current_datetime():
    current_date= datetime.datetime.now()
    print("Current date and time:", current_date.strftime('%Y %m %d %H:%M:%S'))


def calculate_future_date():
    futureD = int(input('Enter the number of days to add to the current date: '))
    current_date = datetime.datetime.now()
    future_date = current_date +  timedelta(days=futureD)
    print("Future date is: ", future_date)

if __name__ == '__main__':
    display_current_datetime()
    calculate_future_date()