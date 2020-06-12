# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2, n):
#             c = a+b
#             a = b
#             b = c
#             print(c)
# fib(15)

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)
    fact(6)
