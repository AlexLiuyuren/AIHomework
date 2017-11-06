//
//  component.hpp
//  AIhomework1
//
//  Created by 刘驭壬 on 2017/10/9.
//  Copyright © 2017年 刘驭壬. All rights reserved.
//

#ifndef component_hpp
#define component_hpp

#include <stdio.h>
#include "string.h"
using namespace std;

struct State{
    //储存了x1, x2, x3
    int state[4];
    //搜索的层数
    int layer;
    //搜索长度
    int searchLength;
    //记录1-9是否使用过
    bool visit[10];
    State(){
        memset(state, 0, 4 * sizeof(int));
        layer = 0;
        searchLength = 0;
        memset(visit, 0, 10 * sizeof(bool));
    }
};

extern int map[];
extern int ans;
void restore(int *state);
bool check(int *state);
void printMap();
void clear();
void printState(State a);


#endif /* component_hpp */
