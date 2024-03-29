from ._builtin import Page, WaitPage


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class P1Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return self.player.role == 'Player 1'

class P2WaitPage(WaitPage):
    title_text = ''
    body_text = 'You are Player 2. Please wait for Player 1 to to make their choice.'

    def is_displayed(self):
        return self.player.role == 'Player 2'


class P2Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        if self.player.role == 'Player 2':
            return self.player.other_player().decision != 'Out'

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'opponent_decision': opponent.decision
        }

class P1WaitPage(WaitPage):
    title_text = ''
    body_text = 'You are Player 1. Please wait for Player 2 to to make their choice.'

    def is_displayed(self):
        return (self.player.role == 'Player 1' and self.player.decision != 'Out')


class P1Decision2(Page):
    form_model = 'player'
    form_fields = ['decision2']

    def is_displayed(self):
        return (self.player.role == 'Player 1' and self.player.other_player().decision != 'Honor'  and self.player.decision != 'Out')


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'opponent': opponent,
            'my_payoff': int(self.player.payoff),
            'opponent_payoff': int(opponent.payoff)
        }


page_sequence = [
    Introduction,
    P1Decision,
    P2WaitPage,
    P2Decision,
    P1WaitPage,
    P1Decision2, 
    ResultsWaitPage,
    Results
]
