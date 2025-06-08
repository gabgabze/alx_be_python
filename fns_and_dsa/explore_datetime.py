import datetime
def display_current_datetime():
    current_date= datetime.datetime.now()
    print("Current date and time:",current_date.strftime('%Y %M %d %H:%M:%S'))

if __name__ == '__main__':
    display_current_datetime()