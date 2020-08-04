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


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group = True)


class Group(BaseGroup):
    finished = models.IntegerField(initial = 0)
    def live_agreement(self, id_in_group, data):
        if(data == 'game_finished'):
            self.finished = self.finished + 1
            return{0: self.finished}


class Player(BasePlayer):
    contract = models.StringField()
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
