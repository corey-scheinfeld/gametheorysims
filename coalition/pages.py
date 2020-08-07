from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 4*60

class IntroWait(WaitPage):
    def after_all_players_arrive(self):
        pass

class Main(Page):
    live_method = 'live_agreement'
    form_model = 'player'
    form_fields = ['contract']

    timer_text = 'Time left to complete this section:'
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3


class Contract(Page):
    def is_displayed(self):
        return (self.get_timeout_seconds() > 3)
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
        return []
    def error_message(self, values):
        group = self.group
        if self.player.contract == 'A and B':
            if values['firmA']+ values['firmB'] != 90:
                return 'The merger profit must total 90'
        if self.player.contract == 'B and C':
            if values['firmB']+ values['firmC'] != 40:
                return 'The merger profit must total 40'
        if self.player.contract == 'A and C':
            if values['firmA']+ values['firmC'] != 70:
                return 'The merger profit must total 70'
        if self.player.contract == 'A, B and C':
            if values['firmA']+ values['firmB'] + values['firmC'] != 100:
                return 'The merger profit must total 100'
    timer_text = 'Time left to complete this section:'
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def before_next_page(self):
        if self.player.merged = True:
            self.player.complete = True
            players = self.player.get_others_in_group()
            for p in players:
                if (p.merged == True and p.complete == True):
                    if ((p.firmA == self.player.firmA) and (p.firmB == self.player.firmB) and (p.firmC == self.player.firmC)):
                        self.group.matching_contract = True
                    else:
                        self.group.matching_contract = False
                        self.group.chances = self.group.chances+1

class double_check(WaitPage):
    title_text = "Contract Finalization"
    body_text = "Please wait while players finalize their merger agreements."
    def after_all_players_arrive(self):
        pass


class second_chance(Page):

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
        return []

    timer_text = 'Time left to complete this section:'
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return ((self.group.chances == 2) and (not(self.group.matching_contract)) and (self.player.merged == True) and (self.get_timeout_seconds() > 3))

class ResultsWaitPage(WaitPage):
    title_text = "Contract Finalization"
    body_text = "Please wait while players finalize their merger agreements."


class Results(Page):
    pass

page_sequence = [Introduction, IntroWait, Main, Contract, double_check, second_chance, ResultsWaitPage, Results]
