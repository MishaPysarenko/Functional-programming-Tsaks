#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

template <typename T>
T pipeline(T data, vector<function<T(T)>> steps) {
    for (auto& step : steps)
        data = step(data);
    return data;
}