from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import math as M
import random as R

author = 'Corey Scheinfeld'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'matching'
    players_per_group = 5
    num_rounds = 2

    instructions_template = 'matching/instructions.html'

    A_role = 'A'
    B_role = 'B'
    C_role = 'C'
    D_role = 'D'
    E_role = 'E'



class Subsession(BaseSubsession):
    def creating_session(self):
        if(self.round_number == 1):
            self.group_randomly()
        else:
            self.group_like_round(1)
        for g in self.get_groups():
                g.assign_ranking()

class Group(BaseGroup):
    

    def assign_ranking(self):
        self.get_player_by_id(1).participant.vars['ranking'] = [1, 3, 2]
        self.get_player_by_id(2).participant.vars['ranking'] = [3, 2, 1]
        self.get_player_by_id(3).participant.vars['ranking'] = [2, 1, 3]
        self.get_player_by_id(4).participant.vars['ranking'] = [2, 1, 3]
        self.get_player_by_id(5).participant.vars['ranking'] = [2, 3, 1]

    def set_payoffs(self):
        s1Priorities = [5, 3, 4, 2, 1]
        s2Priorities = [4, 2, 1, 5, 3]
        s3Priorities = [3, 1, 4, 5, 2]

        s1Match = []
        s2Match = []
        s3Match = []

        group_round = 0
        matching = True

        while(matching):
            matching = False
            group_round +=1
            apps = []
            for p in self.get_players():
                if(p.round == 1):
                    apps.append(p.first)
                elif(p.round == 2):
                    apps.append(p.second)
                elif(p.round == 3):
                    apps.append(p.third)
            for rank, pref in enumerate(s1Priorities):
                if(apps[pref-1] == 1 and self.get_player_by_id(pref).match == 0):
                    if(len(s1Match) < 1):
                        self.get_player_by_id(pref).match = 1
                        s1Match.append(pref)
                    elif(self.round_number == 2):
                        for num, match in enumerate(s1Match):
                            if(rank < s1Priorities.index(match)):
                                self.get_player_by_id(pref).match = 1
                                self.get_player_by_id(match).match = -1
                                s1Match[num] = pref

            for rank, pref in enumerate(s2Priorities):
                if(apps[pref-1] == 2 and self.get_player_by_id(pref).match == 0):
                    if(len(s2Match) < 2):
                        self.get_player_by_id(pref).match = 2
                        s2Match.append(pref)
                    elif(self.round_number == 2):
                        for num, match in enumerate(s2Match):
                            if(rank < s2Priorities.index(match)):
                                self.get_player_by_id(pref).match = 2
                                self.get_player_by_id(match).match = -1
                                s2Match[num] = pref
        
            for rank, pref in enumerate(s3Priorities):
                if(apps[pref-1] == 3 and self.get_player_by_id(pref).match == 0):
                    if(len(s3Match) < 2):
                        self.get_player_by_id(pref).match = 3
                        s3Match.append(pref)
                    elif(self.round_number == 2):
                        for num, match in enumerate(s3Match):
                            if(rank < s3Priorities.index(match)):
                                self.get_player_by_id(pref).match = 3
                                self.get_player_by_id(match).match = -1
                                s3Match[num] = pref

            for p in self.get_players():
                if p.match == 0 or p.match == -1:
                    matching = True
                    p.round +=1
                    p.match = 0

            if(self.round_number == 1 and group_round >= 3):
                matching = False

                    
        for p in self.get_players():
            if(p.participant.vars['ranking'][0] == p.match):
                p.payoff = 300
            elif(p.participant.vars['ranking'][1] == p.match):
                p.payoff = 200
            elif(p.participant.vars['ranking'][2] == p.match):
                p.payoff = 100
        
        

class Player(BasePlayer):
    match = models.IntegerField(initial=0)
    round = models.IntegerField(initial = 1)

    first = models.IntegerField(label = "First Preference", choices=[1,2,3])
    second = models.IntegerField(label = "Second Preference", choices=[1,2,3])
    third = models.IntegerField(label = "Third Preference", choices=[1,2,3])
