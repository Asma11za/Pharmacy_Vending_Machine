class VendingMachine:
    def __init__(self):
        self.state = 'Q0'
    
    def transition(self, input):
        transitions = {
            'Q0': {
                'Op1': 'Q1', 'Op2': 'Q2', 'SelNp': 'Q4', 'SelMR': 'Q5', 'SelSpF': 'Q6',
                'SelPm': 'Q7', 'SelP1': 'Q8', 'SelC': 'Q9', 'CheckAv': 'Q10'
            },
            'Q1': {
                'SelNp': 'Q4', 'SelMR': 'Q5', 'SelSpF': 'Q6', 'CheckAv': 'Q13'
            },
            'Q2': {
                'SelPm': 'Q7', 'SelP1': 'Q8', 'SelC': 'Q9', 'CheckAv': 'Q17'
            },
            'Q4': {
                'CheckAv': 'Q13'
            },
            'Q5': {
                'CheckAv': 'Q14'
            },
            'Q6': {
                'CheckAv': 'Q15'
            },
            'Q7': {
                'CheckAv': 'Q17'
            },
            'Q8': {
                'CheckAv': 'Q18'
            },
            'Q9': {
                'CheckAv': 'Q19'
            },
            'Q13': {
                'Av': 'Q23', 'NotAv': 'Q32'
            },
            'Q14': {
                'Av': 'Q24', 'NotAv': 'Q32'
            },
            'Q15': {
                'Av': 'Q25', 'NotAv': 'Q32'
            },
            'Q17': {
                'Av': 'Q36', 'NotAv': 'Q34'
            },
            'Q18': {
                'Av': 'Q37', 'NotAv': 'Q34'
            },
            'Q19': {
                'Av': 'Q38', 'NotAv': 'Q34'
            },
            'Q23': {
                '10': 'Q26', '15': 'Q27', '5': 'Q28', '55': 'Q29'
            },
            'Q24': {
                '10': 'Q30', '15': 'Q31', '5': 'Q32'
            },
            'Q25': {
                '10': 'Q33', '15': 'Q34', '5': 'Q35'
            },
            'Q26': {
                'Succ': 'Q39', 'NotS': 'Q40'
            },
            'Q27': {
                'Succ': 'Q39', 'NotS': 'Q40'
            },
            'Q28': {
                'Succ': 'Q39', 'NotS': 'Q40'
            },
            'Q29': {
                'Succ': 'Q39', 'NotS': 'Q40'
            },
            'Q30': {
                'Succ': 'Q39', 'NotS': 'Q40'
            },
            'Q31': {
                'Succ': 'Q39', 'NotS': 'Q40'
            },
            'Q32': {
                'Op1': 'Q1', 'Op2': 'Q2', 'SelNp': 'Q4', 'SelMR': 'Q5', 'SelSpF': 'Q6',
                'SelPm': 'Q7', 'SelP1': 'Q8', 'SelC': 'Q9', 'CheckAv': 'Q10'
            }
        }
        
        if input in transitions[self.state]:
            self.state = transitions[self.state][input]
        else:
            print(f"No transition for input '{input}' from state '{self.state}'")

    def process_input(self, inputs):
        for input in inputs:
            self.transition(input)
        return self.state


machine = VendingMachine()

#Example inputs 

inputs = ['Op1', 'SelNp', 'CheckAv', 'Av', '10']
final_state = machine.process_input(inputs)

print(f"Final State: {final_state}")
