#include <iostream>
#include <functional>
#include <vector>
using namespace std;

int apply_rules(int value, vector<function<int(int)>> rules) {
    for (auto& r : rules)
        value = r(value);
    return value;
}