def solution(n):
# 음 그다음에 나머지로 1, 2, 4 개수를 구해야함
# 1의 자리는 3개 10의자리는 9개 100의 자리는 3 3 3 27개 3의 n승 개

    list_124 = ['4', '1', '2']
    s = ''

    while n > 0:
        s += list_124[n%3]
        # 3의 배수일때도 해줘서 -1을 해도 몫은 똑같음 그리고 n이 1일때도 없애주니까
        if n%3 == 0:
            n -= 1


        n //= 3
    return s[::-1]
