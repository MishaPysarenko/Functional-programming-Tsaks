#include <iostream>
#include <functional>
#include <vector>
#include <map>
using namespace std;

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }
int divi(int a, int b) { return a / b; }

int main() {
    map<string, function<int(int, int)>> ops = {
        {"+", add},
        {"-", sub},
        {"*", mul},
        {"/", divi}
    };

    cout << ops["+"](2, 3);
}