def validate(target, rules, conds):
    for animal in target:
        if subvalidate([animal], rules, conds) is True:
            print('animal is %s' % animal)
            break


def subvalidate(cd, rules, conds):
    for x in cd:
        if x in conds:
            continue
        result = False
        S = applicable_rules(rules, x)
        while result is False and len(S) > 0:
            rule = S[0]
            rule.print()
            del S[0]
            r = verify(rule, conds)
            if r is True:
                result = True
            elif subvalidate(rule.condition, rules, conds) is True:
                result = True
        if result is False:
            return False
    return True


def applicable_rules(rules, conds):
    result = []
    for rule in rules:
        if rule.result in conds:
            result.append(rule)
    return result


def verify(rule, conds):
    result = True
    for x in rule.condition:
        if x not in conds:
            result = False
            break
    return result
