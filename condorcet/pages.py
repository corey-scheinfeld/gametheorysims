from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1 or self.round_number==6

class Main(Page):
    def js_vars(self):
    return dict(
        jar_color=self.player.group.jar_type,
    )


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
