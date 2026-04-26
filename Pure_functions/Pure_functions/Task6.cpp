#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

vector<int> sort_numbers(vector<int> nums) {
    vector<int> copy = nums;

    function<void(int, int)> bubble = [&](int n, int i) {
        if (n == 1) return;
        if (i == n - 1) return bubble(n - 1, 0);

        if (copy[i] > copy[i + 1])
            swap(copy[i], copy[i + 1]);

        bubble(n, i + 1);
        };

    bubble(copy.size(), 0);
    return copy;
}