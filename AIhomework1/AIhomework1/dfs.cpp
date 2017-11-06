//
//  dfs.cpp
//  AIhomework1
//
//  Created by 刘驭壬 on 2017/10/7.
//  Copyright © 2017年 刘驭壬. All rights reserved.
//

#include "dfs.hpp"
#include "component.hpp"
#include <iostream>
#include <stack>
#include <vector>

using namespace  std;
void dfs(){
    cout << "dfs result:" << endl;
    cout << "搜索路径：" << endl;
    clear();
    stack<State> st;
    vector<State> res;
    State s;
    //记录搜索长度
    int count = -1;
    //是否找到了第一个解
    bool noAnswer = true;
    bool firstIt = true;
    st.push(s);
    while(!st.empty()){
        State tmp = st.top();
        st.pop();
        count ++;
        if (noAnswer == true && !firstIt) printState(tmp);
        firstIt = false;
        //是否是最后一层
        if (tmp.layer == 3){
            //确定是否是答案
            if (check(tmp.state)){
                tmp.searchLength = count;
                noAnswer = false;
                res.push_back(tmp);
            }
        }else{
            for (int i = 9; i >= 1; i--){
                //跳过已经用过的值
                if (tmp.visit[i] == true) continue;
                //确定下一个状态
                State n = tmp;
                n.layer = tmp.layer + 1;
                n.state[n.layer] = i;
                n.visit[i] = true;
                st.push(n);
            }
        }
    }
    //输出所有答案
    cout << "搜索长度即结果:" << endl;
    vector<State>::iterator it;
    for (it = res.begin(); it != res.end(); it++){
        restore(it->state);
        cout << "search length: " << it->searchLength << endl;
        printMap();
    }
    
}

