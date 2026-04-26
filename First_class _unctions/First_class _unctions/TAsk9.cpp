#include <iostream>
#include <functional>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

vector<int> sort_asc(vector<int> data) {
    sort(data.begin(), data.end());
    return data;
}

vector<int> sort_desc(vector<int> data) {
    sort(data.rbegin(), data.rend());
    return data;
}

int main() {
    map<string, function<vector<int>(vector<int>)>> strategies = {
        {"asc", sort_asc},
        {"desc", sort_desc}
    };
}