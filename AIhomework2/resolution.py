from unify import unify, applys
from expr import Exprs
import copy

# 单表达式消解
# 返回是否能消解，替换的策略
def resolution(expr1, expr2):
    if expr1.name != expr2.name:
        return False, ''
    elif expr1.sign != 1 - expr2.sign:
        return False, ''
    else:
        sub = unify(expr1, expr2)
        if sub == 'Fail':
            return False, ''
        else:
            return True, sub


# 多表达式消解
# 返回是否能替换，替换的结果
def exprs_resolution(exprs1, exprs2):
    new_exprs1 = copy.deepcopy(exprs1)
    new_exprs2 = copy.deepcopy(exprs2)
    len1 = len(exprs1.exprs)
    len2 = len(exprs2.exprs)
    delete1 = [False] * len1
    delete2 = [False] * len2
    change = False
    subs = ''
    first = True
    for i in range(len1):
        for j in range(len2):
            success, sub = resolution(exprs1.exprs[i], exprs2.exprs[j])
            if success is False:
                continue
            else:
                if first is True:
                    subs += sub
                else:
                    if sub != '':
                        subs = subs + ' ' + sub
                change = True
                delete1[i] = True
                delete2[j] = True
                applys(sub, new_exprs1)
                applys(sub, new_exprs2)
    result = Exprs()
    for i in range(len1):
        if delete1[i] is False:
            result.exprs.append(new_exprs1.exprs[i])
    for i in range(len2):
        if delete2[i] is False:
            result.exprs.append(new_exprs2.exprs[i])
    result.parents.extend(new_exprs1.parents)
    result.parents.extend(new_exprs2.parents)
    return change, result, subs


# def conflict(expr1, expr2):
#     if expr1.name == expr2.name:
#         if expr1.symbol == expr2.symbol:
#             if expr1.sign == 1 - expr2.sign:
#                 return True
#     return False