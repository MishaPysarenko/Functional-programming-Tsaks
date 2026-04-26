#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

struct State {
    int value;
};

vector<State> history;

State current_state = { 0 };

void apply(int new_value) {
    history.push_back(current_state);
    current_state = { new_value };
}

void undo() {
    if (!history.empty()) {
        current_state = history.back();
        history.pop_back();
    }
}