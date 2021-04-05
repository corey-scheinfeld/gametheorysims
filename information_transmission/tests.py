from otree.api import Currency as c, currency_range, expect
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):

        yield pages.instructions

        if self.player.id_in_group == 1:
            yield pages.Send, dict(message=5)

        else:
            yield pages.SendBack, dict(action=3)

        yield pages.Results
