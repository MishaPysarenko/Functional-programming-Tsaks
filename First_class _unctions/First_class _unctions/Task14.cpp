#include <iostream>
#include <functional>
#include <vector>
#include <map>
using namespace std;

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }
int square(int a) { return a * a; }

int main() {
    map<string, function<int(int, int)>> engine2 = {
        {"add", add},
        {"mul", mul}
    };

    map<string, function<int(int)>> engine1 = {
        {"square", square}
    };

    cout << engine2["add"](2, 3);
    cout << engine1;
}