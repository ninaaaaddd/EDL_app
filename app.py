from flask import render_template , Flask ,request
from google.oauth2 import service_account
from googleapiclient.discovery import build
import numpy as np
import time
import threading


app = Flask(__name__)

def get_spreadsheet_data():
    # Load the JSON key file for the service account
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = 'keys/key_file.json'
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    sheet_id='1BMUeqPfCKHb5U__U9I2MMZ9cVCYuoB5XOvM8nOXry5c'
    sheet_range="Sheet1!A:I"
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return None
    values1=(values[-5:])
    return values1


@app.route('/' , )
def index():
    # Call the function to retrieve the data from the Google Spreadsheet
    data = get_spreadsheet_data()

    # Render the template with the data
    return render_template('index.html', data=data)


if __name__ == '__main__':
    
    app.run(debug=True)
    # restart_app()