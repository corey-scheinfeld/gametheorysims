from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random
import numpy as np

"""
Sim for 'Repeated Game of Random Length'
 """

class Constants(BaseConstants):
    name_in_url = 'repeatedFlip'
    players_per_group = 2
    instructions_template = 'repeatedFlip/instructions.html'

    delta = 0.50
    num_matches = 3
    match_duration = np.random.geometric(p=(1-delta), size=num_matches) 
    num_rounds = np.sum(match_duration)
    last_rounds = np.cumsum(match_duration)
    last_round = last_rounds[-1]
    first_rounds = [1]
    for k in range(1, len(match_duration)):
        first_rounds.append(int(last_rounds[k - 1] + 1))


class Subsession(BaseSubsession):
    match_number = models.IntegerField()
    round_in_match_number = models.IntegerField()

    def creating_session(self):

        if self.round_number == 1:
            self.session.vars['alive'] = True
        k = 0
        while k < len(Constants.last_rounds):
            if self.round_number <= Constants.last_rounds[k]:
                self.match_number = k + 1
                k = len(Constants.last_rounds)
            else:
                k += 1

        self.round_in_match_number = self.round_number - Constants.first_rounds[self.match_number-1] + 1

        if self.round_number in Constants.first_rounds:
            self.group_randomly()
        else:
            self.group_like_round(self.round_number-1)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField(
        choices=[1, 2],
        widget=widgets.RadioSelect,
        label='Please make your choice.'
    )
    partner_choice = models.IntegerField()
    
    def other_player(self):
        self.participant.vars['opponent'] = self.get_others_in_group()[0].participant.id_in_session
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            1:
                {
                    1: 32,
                    2: 12
                },
            2:
                {
                    1: 50,
                    2: 25
                }
        }
        self.payoff = payoff[self.choice][self.other_player().choice]
        self.partner_choice = self.other_player().choice
    
        
