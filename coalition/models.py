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


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group = True)


class Group(BaseGroup):
    matching_contract = models.BooleanField(initial = False)
    finished_agreement = models.IntegerField(initial = 0)
    chances = models.IntegerField(initial = 0)
    def live_agreement(self, id_in_group, data):
        #moves all players forward after an agreement has been reached between two or more parties
        if(data != 'A, B and C'):
            self.finished_agreement = int(self.finished_agreement) + 1
            self.get_player_by_id(id_in_group).merged = True
            return{0: int(self.finished_agreement)}
        if(data == 'A, B and C'):
            return{0: 0}





class Player(BasePlayer):
    merged = models.BooleanField(initial = False)
    complete = models.BooleanField(initial = False)
    contract = models.StringField(blank=True)
    firmA = models.IntegerField(label = "Firm A Merger Profit:", blank=True)
    firmB = models.IntegerField(label = "Firm B Merger Profit:", blank=True)
    firmC = models.IntegerField(label= "Firm C Merger Profit:", blank=True)


    def contract_choices(self):
        if self.role() == 'A':
            return ['A and B', 'A and C', 'A, B and C']
        if self.role() == 'B':
            return ['A and B', 'B and C', 'A, B and C']
        if self.role() == 'C':
            return ['A and C', 'B and C', 'A, B and C']

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        if self.id_in_group == 2:
            return 'B'
        if self.id_in_group == 3:
            return 'C'

    def chat_nickname(self):
        return 'Company {}'.format(self.role())

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
