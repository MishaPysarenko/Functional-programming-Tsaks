#include <iostream>
using namespace std;

/* =======================
   гбхвюимю пейспя╡ъ
   ======================= */
void printReverseRec(const string& s, int i) {
    if (i < 0) return;
    cout << s[i];
    printReverseRec(s, i - 1);
}

/* =======================
   убнярнбю пейспя╡ъ
   ======================= */
void fillReverseTail(const string& s, int i, char* res, int n) {
    if (i == n) return;
    res[n - 1 - i] = s[i];
    fillReverseTail(s, i + 1, res, n);
}

void printReverseTail(const string& s) {
    int n = s.size();
    char* res = new char[n + 1];
    fillReverseTail(s, 0, res, n);
    res[n] = '\0';

    cout << res;

    delete[] res;
}