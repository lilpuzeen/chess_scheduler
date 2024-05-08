from google.oauth2.service_account import Credentials
from plugins.config import settings
from datetime import datetime

import gspread

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_info(
	{
		'private_key': settings.GOOGLE_PRIVATE_KEY.replace('\\n', '\n'),
		'private_key_id': settings.GOOGLE_PRIVATE_KEY_ID,
		'client_email': settings.GOOGLE_CLIENT_EMAIL,
		'client_id': settings.GOOGLE_CLIENT_ID,
		'token_uri': settings.GOOGLE_TOKEN_URI,
		'type': 'service_account'
	}, scopes=scopes
)
client = gspread.authorize(credentials)

sheet_id = settings.GOOGLE_SHEET_ID
wb = client.open_by_key(sheet_id)


def get_time_control() -> str:
	ws = wb.worksheet("Весна 2023/2024")
	today = datetime.now().strftime("%d.%m")
	time_control = ws.cell(ws.find(today).row, 4).value.split("+")
	return f"{{min: {int(time_control[0].strip())}, sec: {int(time_control[1].strip())}}}"


if __name__ == '__main__':
    print(get_time_control())
