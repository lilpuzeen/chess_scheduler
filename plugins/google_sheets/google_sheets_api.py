import gspread
from google.oauth2.service_account import Credentials

from plugins.config import (
	GOOGLE_PRIVATE_KEY,
	GOOGLE_PRIVATE_KEY_ID,
	GOOGLE_CLIENT_EMAIL,
	GOOGLE_CLIENT_ID,
	GOOGLE_TOKEN_URI,
	GOOGLE_SHEET_ID
)

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