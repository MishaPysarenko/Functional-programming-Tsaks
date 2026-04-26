#include <iostream>
#include <functional>
#include <vector>
using namespace std;

vector<int> pipeline(vector<int> data, vector<function<vector<int>(vector<int>)>> steps) {
    for (auto& step : steps)
        data = step(data);
    return data;
}