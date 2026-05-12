class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        pre = init
        for i in range(0,iterations):
            pre = pre - 2*(pre * learning_rate)
        return round(pre, 5)
