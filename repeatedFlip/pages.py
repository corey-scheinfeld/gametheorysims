from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1 


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()

class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'player_payoff': int(self.player.payoff),
            'opponent_choice': opponent.choice,
            'opponent_payoff': int(opponent.payoff)
        }
    
    def before_next_page(self):
        self.player.participant.vars['waiting'] = True


class Rematch(Page):
    def is_displayed(self):
        return self.subsession.round_number in Constants.last_rounds
    

class End(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.last_round


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Rematch, 
    End
]
