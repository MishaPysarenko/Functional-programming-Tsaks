#include <iostream>
#include <vector>
#include <functional>
using namespace std;
function<int(int)> compose_many(vector<function<int(int)>> funcs) {
    return [funcs](int x) {
        for (auto& f : funcs)
            x = f(x);
        return x;
        };
}