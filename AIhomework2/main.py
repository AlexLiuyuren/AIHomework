from expr import Expr, Exprs
from bfs import bfs
from dfs import dfs

if __name__ == '__main__':
    # 记录输入信息
    file = open("input.txt", "r")
    list_lines = file.readlines()
    list_exprs = []
    num = int(list_lines[0])
    for i in range(1, num+1):
        tmp = Exprs(list_lines[i])
        list_exprs.append(tmp)
    for x in list_exprs:
        x.print()
    bfs(list_exprs)
    S = [list_exprs[-1]]
    dfs(S, list_exprs)
