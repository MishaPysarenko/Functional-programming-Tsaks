#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

vector<int> pipeline(vector<int> data) {
    vector<int> result;

    for (int x : data)
        if (x % 2 == 0)
            result.push_back(x * x);

    return result;
}