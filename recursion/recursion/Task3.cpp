/* =======================
   гбхвюимю пейспя╡ъ
   ======================= */
int fibRec(int n) {
    if (n <= 1) return n;
    return fibRec(n - 1) + fibRec(n - 2);
}

/* =======================
   убнярнбю пейспя╡ъ
   ======================= */
int fibTail(int n, int a = 0, int b = 1) {
    if (n == 0) return a;
    if (n == 1) return b;
    return fibTail(n - 1, b, a + b);
}