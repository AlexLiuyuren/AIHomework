def generate(target, rules, conds):
    S = applicable_rules(rules, conds)
    while len(S) > 0:
        S[0].print()
        r = apply(S[0], conds)
        # print(r)
        if r != 'None':
            if r in target:
                print('animal is %s' % r)
                break
            else:
                conds.append(r)
                generate(target, rules, conds)
        del S[0]
        if r != 'None':
            del conds[-1]


def applicable_rules(rules, conds):
    result = []
    for rule in rules:
        deduce = True
        for x in rule.condition:
            if x not in conds:
                deduce = False
                break
            if rule.result in conds:
                deduce = False
                break
        if deduce is True:
            result.append(rule)
    return result


def apply(rule, conds):
    deduce = True
    for x in rule.condition:
        if x not in conds:
            deduce = False
            break
    if deduce is True:
        return rule.result
    else:
        return 'None'