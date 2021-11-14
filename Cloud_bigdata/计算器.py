one = float(input("请输入第一个数："))
two = float(input("请输入第二个数："))
oper = input("请输入运算符 + - * / ：")
if oper == '+':
    print(one + two)
elif oper == '-':
    print(one - two)
elif oper == '*':
    print(one * two)
elif oper == '/':
    if two == 0:
        print("除数不能是0")
    else:
        print(one / two)
