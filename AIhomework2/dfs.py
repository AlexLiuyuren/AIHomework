import copy
from resolution import exprs_resolution


def dfs(S, T):
    new_t = copy.deepcopy(T)
    sorted(new_t, key=lambda x: len(x.exprs))
    stack = []
    for x in S:
        stack.append(copy.deepcopy(x))
    finish = False
    num = 0
    while len(stack) != 0 and finish is False:
        exprs = stack.pop()
        for i in range(len(new_t)):
            change, result, subs = exprs_resolution(exprs, new_t[i])
            if change is True:
                num += 1
                stack.append(result)
                new_t.append(result)
                print('合一步骤%d为: ' % num)
                print(subs)
                print('消解步骤%d为:' % num)
                exprs.print()
                new_t[i].print()
                result.print()
                print('\n')
                if len(result.exprs) == 0:
                    finish = True
                    break
        sorted(new_t, key=lambda x: len(x.exprs))
    if finish is True:
        print('消解完成，最终结论正确')
    else:
        print('消解失败，最终结论错误')
    return
