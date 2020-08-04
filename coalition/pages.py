from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Main(Page):
    form_model = 'player'
    form_fields = ['contract', 'personal', 'firm1', 'firm2']

    def error_message(self, values):
        if(values['contract'] == 'A and B'):
            if((values[personal]+values[firm1]+values[firm2]) != 90):
                return 'The profit must add up to 90'
        if(values['contract'] == 'A and C'):
            if((values[personal]+values[firm1]+values[firm2]) != 70):
                return 'The profit must add up to 70'
        if(values['contract'] == 'B and C'):
            if((values[personal]+values[firm1]+values[firm2]) != 40):
                return 'The profit must add up to 40'
        if(values['contract'] == 'A, B, and C'):
            if((values[personal]+values[firm1]+values[firm2]) != 100):
                return 'The profit must add up to 100'

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Introduction, Main, ResultsWaitPage, Results]
