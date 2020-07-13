from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class Main(Page):
    form_model = 'player'
    form_fields = ['sent_tokens', 'private_tokens']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive1 = 'set_ratio'
    after_all_players_arrive2 ='set_payoffs'



class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
