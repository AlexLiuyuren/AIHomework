from expr import Exprs, Expr
import copy

def unify(expr1, expr2):
    symbol1 = expr1.symbol
    symbol2 = expr2.symbol
    # 如果expr1, expr2是常元或者空表
    if ((expr1.name == 'null' and len(symbol1) == 1 and symbol1[0].lower() == symbol1[0]) or (expr1.name == 'null' and \
        len(symbol1) == 0)) and ((expr2.name == 'null' and len(symbol2) == 1 and symbol2[0].lower() == symbol2[0]) or \
        (expr2.name == 'null' and len(symbol2) == 0)):
        if expr1.equal(expr2):
            return ''
        else:
            return 'Fail'
    # 如果expr11是一个变元
    if expr1.name == 'null' and len(symbol1) == 1 and symbol1[0].lower() != symbol1[0]:
        if symbol1[0] in symbol2:
            return 'Fail'
        else:
            return '%s/%s' % (symbol2[0], symbol1[0])
    # 如果expr2是一个变元
    elif expr2.name == 'null' and len(symbol2) == 1 and symbol2[0].lower() != symbol2[0]:
        if symbol2[0] in symbol1:
            return 'Fail'
        else:
            return '%s/%s' % (symbol1[0], symbol2[0])

    # 其他情况
    else:
        he1 = Expr(1, 'null', [expr1.symbol[0]])
        he2 = Expr(1, 'null', [expr2.symbol[0]])
        subs1 = unify(he1, he2)
        if subs1 == 'Fail':
            return 'Fail'
        new_expr1 = copy.deepcopy(expr1)
        new_expr2 = copy.deepcopy(expr2)
        del new_expr1.symbol[0]
        del new_expr2.symbol[0]
        if len(new_expr1.symbol) == 0:
            new_expr1.name = 'null'
            new_expr1.sign = 1
        if len(new_expr2.symbol) == 0:
            new_expr2.name = 'null'
            new_expr2.sign = 1
        apply(subs1, new_expr1)
        apply(subs1, new_expr2)
        subs2 = unify(new_expr1, new_expr2)
        if subs2 == 'Fail':
            return 'Fail'
        else:
            if subs2 == '':
                return subs1
            else:
                return subs1 + ' ' + subs2


# apply expr
def apply(sub, expr):
    if '/' not in sub:
        return
    subs = sub.split(' ')
    for s in subs:
        ele1, ele2 = s.split('/')
        for i in range(len(expr.symbol)):
            if expr.symbol[i] == ele2:
                expr.symbol[i] = ele1
    return


# apply Exprs
def applys(sub, exprs):
    for i in range(len(exprs.exprs)):
        apply(sub, exprs.exprs[i])
    return