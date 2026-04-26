#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

// FUNCTIONAL CORE (pure)
double compute_total(const vector<int>& items) {
    double sum = 0;
    for (int x : items) sum += x;
    return sum * 1.2;
}

// IMPERATIVE SHELL
double process_order(const map<string, vector<int>>& order) {
    cout << "Processing order..." << endl;
    return compute_total(order.at("items"));
}