#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

struct Transaction {
    int amount;
    string currency;
};

vector<Transaction> filter_usd(const vector<Transaction>& t) {
    vector<Transaction> res;
    for (auto& x : t)
        if (x.currency == "USD")
            res.push_back(x);
    return res;
}

vector<double> convert(const vector<Transaction>& t, double rate) {
    vector<double> res;
    for (auto& x : t)
        res.push_back(x.amount * rate);
    return res;
}

double sum(const vector<double>& v) {
    double s = 0;
    for (double x : v) s += x;
    return s;
}