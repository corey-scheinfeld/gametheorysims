from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 4*60

class Main(Page):
    form_model = 'player'
    form_fields = ['contract']

    timer_text = 'Time left to complete this section:'
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class Contract(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.contract == 'A and B':
            return ['firmA', 'firmB']
        if self.player.contract == 'B and C':
            return ['firmB', 'firmC']
        if self.player.contract == 'A and C':
            return ['firmA', 'firmC']
        if self.player.contract == 'A, B and C':
            return ['firmA', 'firmB', 'firmC']
    def error_message(self, values):
        group = self.group
        if self.player.contract == 'A and B':
            if values['firmA']+ values['firmB'] != 90:
                return 'The merger profit must total 90'
            if group.get_player_by_role('A').firmA != group.get_player_by_role('B').firmA:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_role('A').firmB != group.get_player_by_role('B').firmB:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
        if self.player.contract == 'B and C':
            if values['firmB']+ values['firmC'] != 40:
                return 'The merger profit must total 40'
            if group.get_player_by_role('B').firmB != group.get_player_by_role('C').firmB:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_role('B').firmC != group.get_player_by_role('C').firmC:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
        if self.player.contract == 'A and C':
            if values['firmA']+ values['firmC'] != 70:
                return 'The merger profit must total 70'
            if group.get_player_by_role('A').firmA != group.get_player_by_role('C').firmA:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_role('A').firmC != group.get_player_by_role('C').firmC:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
        if self.player.contract == 'A, B and C':
            if values['firmA']+ values['firmB'] + values['firmC'] != 100:
                return 'The merger profit must total 100'
            if group.get_player_by_role('A').firmC != group.get_player_by_role('C').firmC or group.get_player_by_role('B').firmC != group.get_player_by_role('C').firmC:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_role('A').firmB != group.get_player_by_role('C').firmB or group.get_player_by_role('B').firmB != group.get_player_by_role('C').firmB:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_role('A').firmA != group.get_player_by_role('C').firmA or group.get_player_by_role('B').firmA != group.get_player_by_role('C').firmA:
                return 'Contradicting merger contracts. Please enter agreed profit split.'

    timer_text = 'Time left to complete this section:'
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

page_sequence = [Introduction, Main, Contract, ResultsWaitPage, Results]
