from rule import Rule
from generate import generate
from validate import validate
# 已知:有斑点、长脖子、长腿、有奶、有蹄。 询问:这是什么动物呢?

if __name__ == '__main__':
    file = open('input.txt', 'r')
    list_lines = file.readlines()
    target = list_lines[0].split(' ')
    rules = []
    num = int(list_lines[1])
    for i in range(2, 2+num):
        rule = list_lines[i]
        condition, result = rule.split('#')
        condition = condition.split(' ')
        result = result[:-1]
        rules.append(Rule(condition, result))
    num2 = int(list_lines[2+num])
    for i in range(2+num+1, 2+num+1+num2):
        conds = list_lines[i].split(' ')
        conds[-1] = conds[-1][:-1]
        print('generate:')
        generate(target, rules, conds)
        print('')
        print('validate:')
        validate(target, rules, conds)
