
# 닫는 괄호가 나오면, 바로 직전에 열렸었던 괄호가 닫힘
# 열린 괄호가 나오면, 순서대로 쌓아서 저장

# stack -> 순서대로 데이터를 쌓아놓고, 가장 마지막에 생긴 데이터가 먼저 빠져나가는 형태의 자료구조.
def is_correct_parenthesis(string):

    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True



print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))