#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

double total(const vector<int>& items) {
    double s = 0;
    for (int x : items) s += x;
    return s;
}

double apply_discount(double value, double discount) {
    return value * (1 - discount);
}

double apply_tax(double value, double tax) {
    return value * (1 + tax);
}