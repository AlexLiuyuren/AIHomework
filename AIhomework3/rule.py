class Rule:
    def __init__(self, condition, result):
        self.condition = condition
        self.result = result

    def print(self):
        res = ' '.join(self.condition)
        res = res + '==>' + str(self.result)
        print(res)
