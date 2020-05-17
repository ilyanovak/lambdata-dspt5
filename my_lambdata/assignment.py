# ABC
#State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
#(Handle Washington DC and territories like Puerto Rico etc.)
# IN: Comments should start in form '# '
from pandas import DataFrame
# IN: Why import DataFrame if import pandas?
import pandas as pd


def add_state_name(my_df):
    """
    Adds a column of state name to accompnay a corresponding column
    of state abbreviations

    Params:
        my_df (pandas.DataFrame) has a column called abbrev with state abbreviations

    Returns:
        copy of the original dataframe, with another column
    """

    new_df = my_df.copy()
    names_map = {"AL": "ALABAMA",
    "AK": "ALASKA",
    "AZ": "ARIZONA",
    "AR": "ARKANSAS",
    "CA": "CALIFORNIA",
    "CO": "COLORADO",
    "CT": "CONNECTICUT",
    "DE": "DELAWARE",
    "FL": "FLORIDA",
    "GA": "GEORGIA",
    "HI": "HAWAII",
    "ID": "IDAHO",
    "IL": "ILLINOIS",
    "IN": "INDIANA",
    "IA": "IOWA",
    "KS": "KANSAS",
    "KY": "KENTUCKY",
    "LA": "LOUISIANA",
    "ME": "MAINE",
    "MD": "MARYLAND",
    "MA": "MASSACHUSETTS",
    "MI": "MICHIGAN",
    "MN": "MINNESOTA",
    "MS": "MISSISSIPPI",
    "MO": "MISSOURI",
    "MT": "MONTANA",
    "NE": "NEBRASKA",
    "NV": "NEVADA",
    "NH": "NEW HAMPSHIRE",
    "NJ": "NEW JERSEY",
    "NM": "NEW MEXICO",
    "NY": "NEW YORK",
    "NC": "NORTH CAROLINA",
    "ND": "NORTH DAKOTA",
    "OH": "OHIO",
    "OK": "OKLAHOMA",
    "OR": "OREGON",
    "PA": "PENNSYLVANIA",
    "RI": "RHODE ISLAND",
    "SC": "SOUTH CAROLINA",
    "SD": "SOUTH DAKOTA",
    "TN": "TENNESSEE",
    "TX": "TEXAS",
    "UT": "UTAH",
    "VT": "VERMONT",
    "VA": "VIRGINIA",
    "WA": "WASHINGTON",
    "WV": "WEST VIRGINIA",
    "WI": "WISCONSIN",
    "WY": "WYOMING",
    "GU": "GUAM",
    "PR": "PUERTO RICO",
    "VI": "VIRGIN ISLANDS"}
    new_df['state_name'] = new_df["abbrev"].map(names_map)
    return new_df

def split_timestamp(some_df):
    """
    This function splits dates ("MM/DD/YYYY", etc.) into multiple columns

    Params:
        some_df (pandas.DataFrame) has a column called timestamp with dates in object datatype

    Returns:
        copy of the original dataframe, with three new columsn one for year, month, and day.

    """
    # IN: Seems inconsistent to use my_df in first function and some_df here. Maybe just df in both?
    new_some_df = some_df.copy()

    new_some_df['timestamp'] = pd.to_datetime(new_some_df['timestamp'], infer_datetime_format=True)
    # IN: Above is possibly too long. Maybe move second argument to next level
    new_some_df['year'] = new_some_df['timestamp'].dt.year
    new_some_df['month'] = new_some_df['timestamp'].dt.month
    new_some_df['day'] = new_some_df['timestamp'].dt.day
    # IN: Maybe should drop original 'timestamp' column
    return new_some_df

class SplitTimestamp():
    #how to implement a class.
    #create a class that would generate additional number of columns
    #include hour, minutes, seconds in addtion to year, month and day

    """docstring fo SplitTimestamp."""

    # IN: Maybe add comment explaining this function
    def __init__(self, date):
        self.date = date

    # IN: Maybe add comment explaining this function
    def split_date(self):
        return self.date.split("-")


if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    df2 = add_state_name(df)
    print(df2.head())

    df3 = DataFrame({"timestamp":["2010-01-04", "2012-05-04", "2008-11-02"]})
    print(df3.head())

    df4 = split_timestamp(df3)
    print(df4.head())


    #class test code below
    date_ex = SplitTimestamp("12-01-05")
    print(date_ex.date)
