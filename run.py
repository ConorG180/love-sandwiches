import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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


def update_worksheet(user_inputs, sheet):
    """
    Function for updating the a worksheet
    """
    print(f"Updating {sheet} worksheet")
    sheet = SHEET.worksheet(sheet)
    sheet.append_row(user_inputs)
    print(f"{sheet} worksheet Updated!")


def calculate_surplus(sales_data):
    """
    Function for calculating surplus sandwiches
    """
    stock_data = SHEET.worksheet("stock").get_all_values()
    stock_row = stock_data[(len(stock_data)-1)]
    sales_row = sales_data
    surplus_row = []
    for i, j in zip(stock_row, sales_row):
        calculation = int(i) - j
        surplus_row.append(calculation)
    pprint(surplus_row)
    return surplus_row


def main():
    """
    These are the main functions to run the programme.
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    surplus_data = calculate_surplus(sales_data)
    update_worksheet(surplus_data, "surplus")
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


main()