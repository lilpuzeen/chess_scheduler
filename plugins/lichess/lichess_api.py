import berserk
from berserk.clients.tournaments import Tournaments

from plugins.config import settings


def create_arena():
	session = berserk.TokenSession(settings.LICHESS_TOKEN)
	client = Tournaments(session=session)
	return client.create_arena(
		clockTime=5,
		clockIncrement=2,
		minutes=90,
	)
