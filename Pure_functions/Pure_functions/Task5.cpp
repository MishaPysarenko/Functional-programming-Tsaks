#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

map<string, string> update_age(map<string, string> user, string new_age) {
    user["age"] = new_age;
    return user;
}