//
//  main.cpp
//  AIhomework1
//
//  Created by 刘驭壬 on 2017/10/7.
//  Copyright © 2017年 刘驭壬. All rights reserved.
//

#include <iostream>
#include <set>
#include "component.hpp"
#include "dfs.hpp"
#include "bfs.hpp"
#include "heuristic.hpp"
using namespace std;


int main(int argc, const char * argv[]) {
    freopen("result.txt", "w", stdout);
    dfs();
    bfs();
    heuristic(true);//使用L1距离，定义见heuristic.cpp
    heuristic(false);//使用L2距离
    return 0;
}
