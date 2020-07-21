from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class IntroductionWaitpage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'shuffle_session', 'set_up'


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):
    pass




class Results(Page):
    pass


page_sequence = [
    Introduction,
    IntroductionWaitpage,
    Main,
    ResultsWaitPage,
    Results
]
