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
    total_payoff = models.CurrencyField()
    def set_payoffs(self):
        players = self.get_players()
        contributions = [p.sent_tokens for p in players]
        total_payoff = sum(contributions)
        self.total_contribution = 11*(self.total_payoff) - (1/16)*(self.total_payoff)^2
        for p in players:
            set_ratio(p.sent_tokens)
            p.payoff = p.private_tokens+((p.ratio)*self.total_contribution)



class Player(BasePlayer):
    ratio = models.CurrencyField()
    sent_tokens = models.CurrencyField(min = 0, max = Constants.endowment, label = "Pool Tokens")
    private_tokens = models.CurrencyField(min = 0, max = Constants.endowment, label = "Private Tokens")
    def set_ratio(self.sent_tokens):
        self.ratio = self.sent_tokens / Group.total_payoff
