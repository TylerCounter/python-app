#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int get_index(vector<int> v, int K){
    auto it = find(v.begin(), v.end(), K);
    if (it != v.end()){
        int index = it - v.begin();
        return index;}
    else {return -1;}
}
