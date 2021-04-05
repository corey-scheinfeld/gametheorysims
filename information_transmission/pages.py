from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Introduction(Page):
    def is_displayed(self):
        return (self.round_number == 1 or self.round_number==5)


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['message']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        rand_number = random.randint(1,5)
        self.group.state = rand_number*2 - 1
        return {
            "rand_number":rand_number,
        }
class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['action']

    def is_displayed(self):
        return self.player.id_in_group == 2



class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    """This page displays the earnings of each player"""


page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
