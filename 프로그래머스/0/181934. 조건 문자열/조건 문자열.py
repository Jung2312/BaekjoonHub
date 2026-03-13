def solution(ineq, eq, n, m):
    eq = eq if eq == '=' else ''

    answer = 1 if eval(f"{n}{ineq}{eq}{m}") else 0

    return answer