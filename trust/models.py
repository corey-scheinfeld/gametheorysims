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


doc = """
Simple trust game
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 5

    endowment = c(10)
    multiplier = 3

    instructions_template = 'trust/instructions.html'
    p1_role = 'Player A'
    p2_role = 'Player B'


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=c(0), max=Constants.endowment, doc="""Amount sent by P1"""
    )

    sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""")

    def sent_back_amount_choices(self):
        return currency_range(c(0), self.sent_amount * Constants.multiplier, c(1))

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount



class Player(BasePlayer):
    pass


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'sent', 'recieved', 'payoff']
    for p in players:
        if(p.id_in_group == 1):
            role = "Player A"
            sent =  p.group.sent_amount
            recieved = p.group.sent_back_amount
        else:
            role = "Player B"
            recieved =  p.group.sent_amount
            sent = p.group.sent_back_amount
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, role, sent, recieved, p.payoff]
