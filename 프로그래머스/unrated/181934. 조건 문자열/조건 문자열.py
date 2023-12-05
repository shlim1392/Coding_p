def solution(ineq, eq, n, m):
    return 1 if (ineq == "<" and eq == "=" and n <= m) or \
                (ineq == ">" and eq == "=" and n >= m) or \
                (ineq == "<" and eq == "!" and n < m) or \
                (ineq == ">" and eq == "!" and n > m) else 0

# eval 문자열로 표현된 파이썬 표현식을 인수로 받아 평가하고 결과를 반환
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
