#include <iostream>
#include <vector>
#include <functional>
using namespace std;
function<int(int)> compose(function<int(int)> f,
    function<int(int)> g) {
    return [f, g](int x) {
        return f(g(x));
        };
}