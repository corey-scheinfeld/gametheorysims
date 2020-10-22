from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyWaitPage(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.round_number == 1

class partisan(Page):
    form_model = 'player'
    form_fields = ['affiliation']

    def is_displayed(self):
        return self.round_number == 1

class GroupWaitPage(WaitPage):
    def is_displayed(self):
         return self.round_number == 1
    after_all_players_arrive = 'adjust_group'

class group_display(Page):
    pass

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyWaitPage, partisan, GroupWaitPage, group_display]
