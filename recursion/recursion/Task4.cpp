/* =======================
   гбхвюимю пейспя╡ъ
   ======================= */
int climbRec(int n) {
    if (n <= 2) return n;
    return climbRec(n - 1) + climbRec(n - 2);
}

/* =======================
   убнярнбю пейспя╡ъ
   ======================= */
int climbTail(int n, int a = 1, int b = 2) {
    if (n == 1) return a;
    if (n == 2) return b;
    return climbTail(n - 1, b, a + b);
}