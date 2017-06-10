"""
Notes:

Google spreadsheet API reference: https://gspread.readthedocs.io/en/latest/

IMPORTANT! Improved wrapper for gspread API: https://github.com/nithinmurali/pygsheets

"""


import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
start_time_utc = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S %Z %Y")

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("<<THY-SPREADSHEET-NAME>>").sheet1

# insert code here

