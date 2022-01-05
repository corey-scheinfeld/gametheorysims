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
Battle of the Sexes
"""


class Constants(BaseConstants):
    name_in_url = 'battle'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'battle/instructions.html'
    row_role = 'row'
    column_role = 'column'



class Subsession(BaseSubsession):
    def creating_session(subsession):
        subsession.group_randomly()


class Group(BaseGroup):
    def set_payoffs(self):
        player1 = self.get_player_by_role(Constants.row_role)
        player2 = self.get_player_by_role(Constants.column_role)
        player1.partner_choice = player2.choice
        player2.partner_choice = player1.choice
        if player1.choice == True and player2.choice == True:
            player1.payoff = 600
            player2.payoff = 200
        if player1.choice == True and player2.choice == False:
            player1.payoff = 0
            player2.payoff = 0
        if player1.choice == False and player2.choice == False:
            player1.payoff = 200
            player2.payoff = 600
        if player1.choice == False and player2.choice == True:
            player1.payoff = 0
            player2.payoff = 0

class Player(BasePlayer):
    choice = models.BooleanField()
    partner_choice = models.BooleanField()

def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'choice', 'partner_choice', 'payoff']
    for p in players:
        if(p.choice == 1):
            pchoice = 'Movie'
        else:
            pchoice='Concert'
        if(p.partner_choice == 1):
            partchoice = 'Movie'
        else:
            partchoice='Concert'
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, pchoice, partchoice, p.payoff]
