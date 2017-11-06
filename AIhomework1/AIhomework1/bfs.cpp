//
//  bfs.cpp
//  AIhomework1
//
//  Created by 刘驭壬 on 2017/10/9.
//  Copyright © 2017年 刘驭壬. All rights reserved.
//

//该文件架构和dfs完全相同，仅仅是栈换成了队列，不多加备注
#include "bfs.hpp"
#include "component.hpp"
#include <iostream>
#include <queue>

using namespace  std;
void bfs(){
    cout << "bfs result:" << endl;
    cout << "搜索路径：" << endl;
    clear();
    queue<State> q;
    vector<State> res;
    State s;
    int count = -1;
    bool noAnswer = true;
    bool firstIt = true;
    q.push(s);
    while(!q.empty()){
        State tmp = q.front();
        q.pop();
        count++;
        if (noAnswer == true && !firstIt) printState(tmp);
        firstIt = false;
        //是否是最后一层
        if (tmp.layer == 3){
            //确定是否是答案
            if (check(tmp.state)){
                noAnswer = false;
                tmp.searchLength = count;
                res.push_back(tmp);
            }
        }else{
            for (int i = 1; i <= 9; i++){
                if (tmp.visit[i] == true) continue;
                State n = tmp;
                n.layer = tmp.layer + 1;
                n.state[n.layer] = i;
                n.visit[i] = true;
                q.push(n);
            }
        }
    }
    cout << "搜索长度即结果:" << endl;
    vector<State>::iterator it;
    for (it = res.begin(); it != res.end(); it++){
        restore(it->state);
        cout << "search length: " << it->searchLength << endl;
        printMap();
    }
    
}


