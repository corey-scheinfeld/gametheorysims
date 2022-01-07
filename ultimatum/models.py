from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Currency as c
)
import random

"""
Sim for Ultimatum/Two-Stage Bargaining Game
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = 4

    instructions_template = 'ultimatum/instructions.html'
    role = random.choice([1, 2])
    prop_role = 'Proposer'
    resp_role = 'Responder'
    endowment = c(100)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group= True)

        new_matrix = []
        matrix = self.get_group_matrix()
        
        if(self.round_number == 2):
            for group in matrix:
                new_matrix.append([group[1], group[0]])      
            self.set_group_matrix(new_matrix)


class Group(BaseGroup):
    offer = models.CurrencyField(min=0, max=Constants.endowment, label='')
    responder_choice = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[[True, 'Accept'], [False, 'Reject']],
        label='')
    counter = models.CurrencyField(min=0, max=25, label='')
    proposer_choice = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[[True, 'Accept'], [False, 'Reject']],
        label='')


class Player(BasePlayer):

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.group.responder_choice:
            self.group.get_player_by_role('Responder').payoff = self.group.offer
            self.group.get_player_by_role('Proposer').payoff = Constants.endowment - self.group.offer
        else:
            if self.round_number > 2 and self.group.proposer_choice:
                self.group.get_player_by_role('Proposer').payoff = self.group.counter
                self.group.get_player_by_role('Responder').payoff = 25 - self.group.counter
            else:
                self.payoff = 0
                self.other_player().payoff = 0


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'offer', 'counter_offer', 'choice', 'partner_choice', 'payoff']
    for p in players:
        if(p.role == "Proposer"):
            if(p.group.proposer_choice):
                choice = "Accept"
            elif p.round_number <= 2 or p.group.responder_choice:
                choice = "None"
            else:
                choice = "Reject"

            if(p.group.responder_choice):
                pchoice = "Accept"
            else:
                pchoice = "Reject"
        else:
            if(p.group.proposer_choice):
                pchoice = "Accept"
            elif p.round_number <= 2 or p.group.responder_choice:
                pchoice = "None"
            else:
                pchoice = "Reject"

            if(p.group.responder_choice):
                choice = "Accept"
            else:
                choice = "Reject"
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, p.group.offer, p.group.counter, choice, pchoice, p.payoff]
