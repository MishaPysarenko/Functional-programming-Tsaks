#include <iostream>
#include <vector>
#include <functional>
using namespace std;
vector<int> pipeline(vector<int> data,
    vector<function<vector<int>(vector<int>)>> steps) {
    for (auto& step : steps)
        data = step(data);
    return data;
}

void main() {
    auto result = pipeline(
        { 1,2,3,4,5 },
    {
        [](vector<int> xs) {
            vector<int> res;
            for (int x : xs)
                if (x % 2 == 0)
                    res.push_back(x);
            return res;
        },
        [](vector<int> xs) {
            vector<int> res;
            for (int x : xs)
                res.push_back(x * x);
            return res;
        }
    }
    );
}