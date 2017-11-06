import copy
import queue
from resolution import exprs_resolution

def bfs(exprss):
    exprs_set = copy.deepcopy(exprss)
    length = len(exprs_set)
    for i in range(length):
        exprs_set[i].parents.append(i)
    q = queue.Queue()
    for x in exprs_set:
        q.put(copy.deepcopy(x))
    finish = False
    num = 0
    while q.empty() is False and finish is False:
        exprs = q.get()
        for i in range(len(exprs_set)):
            if i in exprs.parents:
                continue
            else:
                change, result, subs = exprs_resolution(exprs, exprs_set[i])
                if change is True:
                    num += 1
                    result.parents.append(length)
                    exprs_set.append(result)
                    length += 1
                    q.put(result)
                    print('合一步骤%d为:' % num)
                    print(subs)
                    print('消解步骤%d为:' % num)
                    exprs.print()
                    exprs_set[i].print()
                    result.print()
                    print('\n')
                    if len(result.exprs) == 0:
                        finish = True
                        break
    if finish is True:
        print('消解完成，最终结论正确')
    else:
        print('消解失败，最终结论错误')
    return