#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

vector<int> add_item(const vector<int>& items, int item) {
    vector<int> result = items;
    result.push_back(item);
    return result;
}