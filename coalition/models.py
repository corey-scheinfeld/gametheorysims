from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Corey Scheinfeld'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'coalition'
    players_per_group = 3
    num_rounds = 4

    instructions_template = 'coalition/instructions.html'
    second_chance = 'coalition/Contract.html'

    A_role = 'A'
    B_role = 'B'
    C_role = 'C'


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group = True)


class Group(BaseGroup):
    partner_match = models.BooleanField(initial = True)
    matching_contract = models.BooleanField(initial = False)
    finished_agreement = models.IntegerField(initial = 0)
    chances = models.IntegerField(initial = 0)
    def live_agreement(self, id_in_group, data):
        recieve = [1, 2, 3]
        recieve.remove(id_in_group)
        self.get_player_by_id(id_in_group).contract = data
        #moves all players forward after an agreement has been reached between two or more parties
        self.get_player_by_id(id_in_group).merged = True
        return{recieve[0]: 0, recieve[1]: 0}
    def reset(self):
        for player in self.get_players():
            player.complete = False
    def checkContracts(self):
        players = self.get_players()
        contracts = [p.contract for p in players]
        if(contracts[0] == contracts[1] == contracts[2]):
            self.partner_match = True
            self.matching_contract = True
        elif(contracts[0] == 'A, B and C' or contracts[1] == 'A, B and C' or contracts[2] == 'A, B and C'):
            self.partner_match = False
            self.matching_contract = False
        elif(contracts[0] == contracts[1]):
            self.partner_match = True
            players[2].merged = False
            players[2].contract = None
        elif(contracts[0] == contracts[2]):
            self.partner_match = True
            players[1].merged = False
            players[1].contract = None
        elif(contracts[1] == contracts[2]):
            self.partner_match = True
            players[0].merged = False
            players[0].contract = None
        else:
            self.partner_match = False
            self.matching_contract = False



class Player(BasePlayer):
    merged = models.BooleanField(initial = False)
    complete = models.BooleanField(initial = False)
    contract = models.StringField(blank=True)
    firmA = models.IntegerField(label = "Firm A Merger Profit:",initial = 0, min = 0)
    firmB = models.IntegerField(label = "Firm B Merger Profit:", initial = 0, min = 0)
    firmC = models.IntegerField(label= "Firm C Merger Profit:", initial = 0, min = 0)

    def chat_nickname(self):
        return 'Company {}'.format(self.role)

    def chat_configs(self):
        configs = []
        for other in self.get_others_in_group():
            if other.id_in_group < self.id_in_group:
                lower_id, higher_id = other.id_in_group, self.id_in_group
            else:
                lower_id, higher_id = self.id_in_group, other.id_in_group
            configs.append({
                # make a name for the channel that is the same for all
                # channel members. That's why we order it (lower, higher)
                'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
                'label': 'Chat with {}'.format(other.chat_nickname())
            })
        return configs

