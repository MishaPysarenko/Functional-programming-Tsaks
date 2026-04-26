#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

int double_fn(int x) {
    return x * 2;
}

// expression:
// double(5) + double(5)
// becomes:
int result = 10 + 10;  // = 20