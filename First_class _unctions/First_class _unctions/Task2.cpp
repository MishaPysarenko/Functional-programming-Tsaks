#include <iostream>
#include <functional>
#include <vector>
using namespace std;

int add_one(int x) { return x + 1; }
int double_fn(int x) { return x * 2; }
int square_fn(int x) { return x * x; }

int main() {
    vector<function<int(int)>> ops = { add_one, double_fn, square_fn };

    int x = 10;

    for (auto& f : ops)
        cout << f(x) << " ";
}