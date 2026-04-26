#include <iostream>
#include <functional>
#include <vector>
using namespace std;

vector<int> apply_tax(vector<int> data) {
    vector<int> res = data;
    for (int& x : res) x *= 1.2;
    return res;
}

vector<int> apply_discount(vector<int> data) {
    vector<int> res = data;
    for (int& x : res) x *= 0.9;
    return res;
}