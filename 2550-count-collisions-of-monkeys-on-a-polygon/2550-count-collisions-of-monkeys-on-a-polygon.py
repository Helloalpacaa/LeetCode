class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        # 快速幂: pow(base, exp, mod)
        return (pow(2, n, MOD) - 2) % MOD