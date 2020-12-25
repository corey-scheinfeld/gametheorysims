from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
from random import shuffle


"""
Sim for Voluntary Contributions with Punishment game - code pulled from first VC game
"""


class Constants(BaseConstants):
    name_in_url = 'punishment'
    players_per_group = None
    num_rounds = 10

    instructions_template = 'punishment/instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):
        group_matrix = []
        players = self.get_players()
        ppg = self.session.config['players_per_group']
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i + ppg])
        self.set_group_matrix(group_matrix)


class Group(BaseGroup):
    group_project = models.IntegerField(initial = 0)
    def set_labels(self):
        labels = [1, 2, 3, 4]
        shuffle(labels)
        x = 0
        for p in self.get_players():
            p.id_in_group = labels[x]
            x = x+1
    def set_pot(self):
        for player in self.get_players():
            self.group_project = self.group_project + player.contribution
        for player in self.get_players():
            player.first_payoff = int(self.group_project*.5) + (20-player.contribution)
    def set_payoff(self):
        for player in self.get_players():
            if player.id_in_group == 1:
                player.deduct_P1 = 0
            elif player.id_in_group == 2:
                player.deduct_P2 = 0
            elif player.id_in_group == 3:
                player.deduct_P3 = 0
            elif player.id_in_group == 4:
                player.deduct_P4 = 0
            player.reduced = player.deduct_P1 +player.deduct_P2 +player.deduct_P3 +player.deduct_P4
            for p in player.get_others_in_group():
                if player.id_in_group == 1:
                    player.punished = player.punished+p.deduct_P1
                elif player.id_in_group == 2:
                    player.punished = player.punished+ p.deduct_P2
                elif player.id_in_group == 3:
                    player.punished = player.punished+ p.deduct_P3
                if player.id_in_group == 4:
                    player.punished = player.punished+ p.deduct_P4
            player.final_payoff = (int((self.group_project*.5)) + (20 - player.contribution)) - (player.punished*3) - player.reduced
            player.actual = int(player.punished*3)



class Player(BasePlayer):
    contribution = models.IntegerField()
    punished = models.IntegerField(initial = 0)
    first_payoff = models.IntegerField(initial = 0)
    final_payoff = models.IntegerField(initial = 0)
    actual = models.IntegerField(initial = 0)
    reduced = models.IntegerField(initial = 0)
    deduct_P1 = models.IntegerField(min= 0, max = 5, label = "Deduct from P1:")
    deduct_P2 = models.IntegerField(min = 0, max = 5, label = "Deduct from P2:")
    deduct_P3 = models.IntegerField(min = 0, max = 5, label = "Deduct from P3:")
    deduct_P4 = models.IntegerField(min = 0, max = 5, label = "Deduct from P4:")

    def contribution_max(self):
        return self.session.config['endowment']
