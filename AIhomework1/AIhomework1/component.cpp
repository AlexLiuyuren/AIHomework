//
//  component.cpp
//  AIhomework1
//
//  Created by 刘驭壬 on 2017/10/9.
//  Copyright © 2017年 刘驭壬. All rights reserved.
//

#include "component.hpp"
#include <iostream>
#include <set>
using namespace std;
/*
 x1  x2 0
 x3  0  0
 0   0  0
 九宫格如上图，由于只要确定了x1, x2, x3, 九宫格也就确定了，所以可以通过这三个值表达一个状态。
 state数组中存放的是[0, x1, x2, x3]
 */

int map[10];
int ans;

//从state恢复出map
void restore(int *state){
    memset(map, 0, 10*sizeof(int));
    if (state[1] == 0 || state[2] == 0 || state[3] == 0) return;
    map[1] = state[1];
    map[2] = state[2];
    map[4] = state[3];
    map[3] = 15 - map[1] - map[2];
    map[7] = 15 - map[1] - map[4];
    map[5] = 15 - map[3] - map[7];
    map[6] = 15 - map[4] - map[5];
    map[8] = 15 - map[2] - map[5];
    map[9] = 15 - map[1] - map[5];
}

//确定某个state是否是解
bool check(int *state){
    restore(state);
    int s1 = map[7] + map[8] + map[9];
    int s2 = map[3] + map[6] + map[9];
    set<int> s;
    
    for (int i = 1; i <=9; i++){
        if (map[i] <= 0 || map[i] > 9 || s1 != 15 || s2 != 15 || s.count(map[i])==1){
            return false;
        }
        s.insert(map[i]);
    }
    return true;
}

//打印map
void printMap(){
    ans++;
    cout << "map " << ans << ":" << endl;
    for (int i = 1; i <= 9; i++){
        cout << map[i] << " ";
        if (i%3==0){
            cout << endl;
        }
    }
    cout << endl;
}

//打印state
void printState(State a){
    for (int i = 1; i <= 3; i++){
        cout << a.state[i] << " ";
    }
    cout << endl;
}

void clear(){
    memset(map, 0, 10*sizeof(int));
    ans = 0;
}
