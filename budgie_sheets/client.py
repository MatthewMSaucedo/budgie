import pygsheets
import pandas as pd


class SheetsClient:
    # write_buffer = None
    # read_buffer = None

    def __init__(self, cred_file_path="../private/creds.json"):
        # authorization
        self.raw_authed_client = pygsheets.authorize(service_file=cred_file_path)

    def write_sheet(self, content_df, filename, new=True):
        # TODO: throw if not given dataframe
        """"""

    def read_sheet(self, filename):
        # TODO:
        """"""


# Create empty dataframe
df = pd.DataFrame()

# open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open("PY to Gsheet Test")

# select the first sheet
wks = sh[0]

# update the first sheet with df, starting at cell B2.
wks.set_dataframe(df, (1, 1))

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
