import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")


def get_sales_data():
    """
    Get sales data from the user
    """
    while True:
        print("Please enter sales data from the previous market.")
        print("Data should be 6 numbers separated by commas")
        print("For example, 24,17,31,22,27,19\n")
        data_str = input("Enter data here")
        print(f"the data you have entered is {data_str}")
        sales_data = data_str.split(",")
        if validate_data(sales_data):
            break

    return sales_data


def validate_data(data):
    """
    Converts user input to int data type and also validates
    the data - checks if user input is of exactly 6 values
    """
    try:
        data = [int(i) for i in data]
        if len(data) != 6:
            raise ValueError(
                f"6 values expected but {len(data)} were given"
            )
        print("data valid Hermano!")
        return True
    except ValueError as e:
        print(f"invalid data Hombre! - {e}, give it another go please.")
        return False


def update_sales_worksheet(user_inputs):
    """
    Function for updating the sales spreadsheet
    """
    print("Updating sales worksheet")
    sales_sheet = SHEET.worksheet("sales")
    sales_sheet.append_row(user_inputs)
    print("Sales worksheet Updated!")


data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(data)
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
