from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Corey Scheinfeld'

doc = """
Common Pool Rescource Game
"""


class Constants(BaseConstants):
    name_in_url = 'pool'
    players_per_group = 8
    num_rounds = 5
    endowment = c(20)

    instructions_template = 'pool/instructions.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contributions = models.CurrencyField()
    def set_payoffs(self):
        players = self.get_players()
        contributions = [p.sent_tokens for p in players]
        self.total_contribution = 11*sum(contributions) - (1/16)*sum(contributions)^2
        for p in players:
            p.payoff = p.private_tokens+((p.ratio)*self.total_contribution)


class Player(BasePlayer):
    ratio = models.CurrencyField()
    sent_tokens = models.CurrencyField(min = 0, max = Constants.endowment, label = "Pool Tokens")
    private_tokens = models.CurrencyField(min = 0, max = Constants.endowment, label = "Private Tokens")
    individual_share = models.CurrencyField()
    def set_ratio(self):
        players = Group.get_players()
        contributions = [p.sent_tokens for p in players]
        self.ratio = self.sent_tokens / sum(contributions)
