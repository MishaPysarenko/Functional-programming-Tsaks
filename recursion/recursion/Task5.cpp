/* =======================
   гбхвюимю пейспя╡ъ
   ======================= */
double powRec(double x, long long n) {
    if (n == 0) return 1;
    if (n < 0) return 1.0 / powRec(x, -n);

    if (n % 2 == 0) {
        double half = powRec(x, n / 2);
        return half * half;
    }
    return x * powRec(x, n - 1);
}

/* =======================
   убнярнбю пейспя╡ъ
   ======================= */
double powTail(double x, long long n, double acc = 1.0) {
    if (n == 0) return acc;
    if (n < 0) return powTail(x, n + 1, acc / x);
    return powTail(x, n - 1, acc * x);
}