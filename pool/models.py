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
    players_per_group = 2
    num_rounds = 5
    endowment = c(20)

    instructions_template = 'pool/instructions.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    total_payoff = models.CurrencyField()
    def set_payoffs(self):
        players = self.get_players()
        contributions = [p.sent_tokens for p in players]
        self.total_payoff = sum(contributions)
        self.total_contribution = 11*(self.total_payoff) - (1/16)*((self.total_payoff)*(self.total_payoff))
        for p in players:
            p.ratio = float(p.sent_tokens/sum(contributions))
            p.individual_share = ((p.ratio)*self.total_contribution)
            p.payoff = (p.private_tokens)*2 + p.individual_share
            p.ratio = p.ratio*100



class Player(BasePlayer):
    ratio = models.FloatField()
    individual_share = models.CurrencyField()
    sent_tokens = models.CurrencyField(min = 0, max = Constants.endowment, label = "Pool Tokens")
    private_tokens = models.CurrencyField(min = 0, max = Constants.endowment, label = "Private Tokens")
    
