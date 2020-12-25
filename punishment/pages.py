from ._builtin import Page, WaitPage
from random import shuffle


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

class roundWaitPage(WaitPage):
    after_all_players_arrive = 'set_labels'


class Main(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ContributionsWaitPage(WaitPage):
    after_all_players_arrive = 'set_pot'


class Deductions(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.id_in_group == 1:
            return ['deduct_P2', 'deduct_P3', 'deduct_P4']
        elif self.player.id_in_group == 2:
            return ['deduct_P1', 'deduct_P3', 'deduct_P4']
        elif self.player.id_in_group == 3:
            return ['deduct_P1', 'deduct_P2', 'deduct_P4']
        elif self.player.id_in_group == 4:
            return ['deduct_P1', 'deduct_P2', 'deduct_P3']

    def vars_for_template(self):
        contributions = [(p.contribution, p.id_in_group) for p in self.group.get_players()]

        return {
            'contributions': contributions,
            'range': range(1, self.session.config['players_per_group'] + 1)
        }


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoff'

class Results(Page):
    pass


page_sequence = [
    Introduction,
    roundWaitPage,
    Main,
    ContributionsWaitPage,
    Deductions,
    ResultsWaitPage,
    Results
]
