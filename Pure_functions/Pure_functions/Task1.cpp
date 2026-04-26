#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

int balance = 100;

// НЕ ЧИСТА (mutable global state)
int withdraw(int amount) {
    balance -= amount;
    return balance;
}

// ЧИСТА
int add(int a, int b) {
    return a + b;
}

// НЕ ЧИСТА (I/O)
void log_message(string msg) {
    cout << msg << endl;
}

// НЕ ЧИСТА (time dependency)
int get_hour() {
    time_t now = time(0);
    tm* ltm = localtime(&now);
    return ltm->tm_hour;
}