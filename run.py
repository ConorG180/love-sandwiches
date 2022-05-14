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
    print("Please enter sales data from the previous market.")
    print("Data should be 6 numbers separated by commas")
    print("For example, 24,17,31,22,27,19/n")
    data_str = input("Enter data here")
    print(f"the data you have entered is {data_str}")
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(data):
    """
    Converts user input to int data type and also validates
    the data - checks if user input is of exactly 6 values
    """
    try:
        if len(data) != 6:
            raise ValueError(
                f"6 values expected but {len(data)} were given"
            )
    except ValueError as e:
        print(f"invalid data Hombre! - {e}, give it another go please.")


get_sales_data()
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
