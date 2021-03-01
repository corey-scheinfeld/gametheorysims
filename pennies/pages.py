from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return (self.round_number == 1 or self.round_number == 5 or self.round_number == 9)


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(self):
        return {
            'round': self.round_number % 4
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()
            p.participant.vars['total'] += int(p.payoff)


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'player_payoff': int(self.player.payoff),
            'opponent_choice': opponent.choice,
            'stage': (self.round_number // 4) + 1,
            'round': self.round_number % 4

        }

    def before_next_page(self):
        for p in self.group.get_players():
            p.participant.vars['total'] = 0


# repeated sequence because groups must be rematched only after every 4 rounds
page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
