from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)
import random

"""
Sim for 'Acquiring a Company' game
"""


class Constants(BaseConstants):
    name_in_url = 'company'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'company/instructions.html'
    seller_role = 'Seller'
    buyer_role = 'Buyer'

class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)

        for group in self.get_groups():
            group.value = c(random.uniform(0, 100))
        
        new_matrix = []
        matrix = self.get_group_matrix()
        
        if(self.round_number == 2):
            for group in matrix:
                new_matrix.append([group[1], group[0]])      
            self.set_group_matrix(new_matrix)
                    


class Group(BaseGroup):
    value = models.CurrencyField(initial=0)
    buyer_value = models.CurrencyField(initial = 0)


class Player(BasePlayer):
    price = models.CurrencyField(min=0, initial=0, label='')
    partner_price = models.CurrencyField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        buyer = self.group.get_player_by_role('Buyer')
        seller = self.group.get_player_by_role('Seller')
        self.group.buyer_value = 1.5 * self.group.value
        if buyer.price >= seller.price:
            buyer.payoff = 1.5 * self.group.value - buyer.price
            seller.payoff = buyer.price
        else:
            buyer.payoff = 0
            seller.payoff = self.group.value
        self.partner_price = self.get_others_in_group()[0].price


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'role', 'bid/price', 'partner bid/price', 'payoff']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.role, p.price, p.get_others_in_group()[0].price, p.payoff]
