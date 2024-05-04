import berserk
from berserk.clients.tournaments import Tournaments

from plugins.config import LICHESS_TOKEN


def create_arena():
	session = berserk.TokenSession(LICHESS_TOKEN)
	client = Tournaments(session=session)
	return client.create_arena(
		
	)