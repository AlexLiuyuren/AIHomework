class Data:
    def __init__(self, value=[]):
        self.value = value
        self.w = 1

    @staticmethod
    def reset_data(data):
        for d in data:
            d.w = 1
        return

    @staticmethod
    def wsum(data):
        rsum = 0
        for d in data:
            rsum += d.w
        return rsum

