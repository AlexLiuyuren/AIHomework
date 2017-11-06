class Expr:
    def __init__(self, sign, name, symbol):
        self.sign = sign
        self.name = name
        self.symbol = symbol

    def print(self):
        print("sign = %d, name = %s, symbol = %s" %(self.sign, self.name, self.symbol))

    def tostring(self):
        tmp = ''
        if self.sign == 0:
            tmp += '!'
        return tmp + self.name + '(' + str(self.symbol) + ')'

    def equal(self, expr):
        if self.sign != expr.sign:
            return False
        if self.name != expr.name:
            return False
        len1 = len(self.symbol)
        len2 = len(expr.symbol)
        if len1 != len2:
            return False
        for i in range(len1):
            if self.symbol[i] != expr.symbol[i]:
                return False
        return True


class Exprs:
    # string形式：0 E X#1 A X
    def __init__(self, str=''):
        self.exprs = []
        self.parents = []
        if len(str) == 0:
            return
        tmp = str.split('#')
        tmp[-1] = tmp[-1][:-1]
        for x in tmp:
            l = x.split(' ')
            sign = l[0]
            name = l[1]
            symbol = l[2:]
            self.exprs.append(Expr(int(sign), name, symbol))

    def print(self):
        print("Exprs:")
        for x in self.exprs:
            x.print()
