//
//  heuristic.cpp
//  AIhomework1
//
//  Created by 刘驭壬 on 2017/10/9.
//  Copyright © 2017年 刘驭壬. All rights reserved.
//

#include "heuristic.hpp"
#include "component.hpp"
#include <queue>
#include <cmath>
#include <iostream>

using namespace std;

int dis[8];
bool isL1;

//计算8个方向的和，记录在dis数组中
void computeDis(int *dis){
    dis[0] = map[1] + map[2] + map[3];
    dis[1] = map[4] + map[5] + map[6];
    dis[2] = map[7] + map[8] + map[9];
    dis[3] = map[1] + map[4] + map[7];
    dis[4] = map[2] + map[5] + map[8];
    dis[5] = map[3] + map[6] + map[9];
    dis[6] = map[1] + map[5] + map[9];
    dis[7] = map[3] + map[5] + map[7];
}

//启发式策略：距离使用曼哈顿距离
int L1(int *dis){
    int len = 0;
    for (int i = 0; i < 8; i++){
        len += fabs(dis[i] - 15);
    }
    return len;
}

//启发式策略：距离使用平方和
int L2(int *dis){
    int len = 0;
    for (int i = 0; i < 8; i++){
        int t = dis[i] - 15;
        len += fabs(t * t);
    }
    return len;
}

//最小优先队列，定义了两个状态哪个离最终状态最近
bool operator < (State a, State b){
    //函数指针，可以是L1或L2
    int (*ptr)(int *);
    if (isL1 == true){
        ptr = L1;
    }else{
        ptr = L2;
    }
    restore(a.state);
    computeDis(dis);
    int len1 = (*ptr)(dis);
    restore(b.state);
    computeDis(dis);
    int len2 = (*ptr)(dis);
    return len1 > len2;
}

//框架和dfs基本一样，将栈换成了最小优先队列
void heuristic(bool L1){
    cout << "heuristic result:" << endl;
    cout << "搜索路径：" << endl;
    isL1 = L1;
    clear();
    priority_queue<State> pq;
    vector<State> res;
    State st;
    int count = -1;
    bool noAnswer = true;
    bool firstIt = true;
    pq.push(st);
    while(!pq.empty()){
        State tmp = pq.top();
        pq.pop();
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
                pq.push(n);
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
