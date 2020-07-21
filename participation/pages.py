from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    after_all_players_arrive = 'creating_session', 'set_group_type'


class Main(page):
    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):




class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
