from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class IntroductionWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_up'



class Main(Page):
    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_participants', 'determine_winner', 'set_payoffs'




class Results(Page):
    pass


page_sequence = [
    Introduction,
    IntroductionWaitPage,
    Main,
    ResultsWaitPage,
    Results
]
