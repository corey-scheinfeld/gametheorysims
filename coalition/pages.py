from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Main(Page):
    form_model = 'player'
    form_fields = ['contract']


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
            if group.get_player_by_id('A').firmA != group.get_player_by_id('B').firmA:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_id('A').firmB != group.get_player_by_id('B').firmB:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
        if self.player.contract == 'B and C':
            if values['firmB']+ values['firmC'] != 40:
                return 'The merger profit must total 40'
            if group.get_player_by_id('B').firmB != group.get_player_by_id('C').firmB:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_id('B').firmC != group.get_player_by_id('C').firmC:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
        if self.player.contract == 'A and C':
            if values['firmA']+ values['firmC'] != 70:
                return 'The merger profit must total 70'
            if group.get_player_by_id('A').firmA != group.get_player_by_id('C').firmA:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_id('A').firmC != group.get_player_by_id('C').firmC:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
        if self.player.contract == 'A, B and C':
            if values['firmA']+ values['firmB'] + values['firmC'] != 100:
                return 'The merger profit must total 100'
            if group.get_player_by_id('A').firmC != group.get_player_by_id('C').firmC or group.get_player_by_id('B').firmC != group.get_player_by_id('C').firmC:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_id('A').firmB != group.get_player_by_id('C').firmB or group.get_player_by_id('B').firmB != group.get_player_by_id('C').firmB:
                return 'Contradicting merger contracts. Please enter agreed profit split.'
            if group.get_player_by_id('A').firmA != group.get_player_by_id('C').firmA or group.get_player_by_id('B').firmA != group.get_player_by_id('C').firmA:
                return 'Contradicting merger contracts. Please enter agreed profit split.'

class Results(Page):
    pass

page_sequence = [Introduction, Main, Contract, Results]
