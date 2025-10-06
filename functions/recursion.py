# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         f = factorial(n-1)
#         result = n * f
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    result = factorial(n) / ((factorial(n - k)) * factorial(k))
    print(f"{n}: {factorial(n)}")
    print(f"{n - k}: {factorial(n - k)}")
    print(f"{k}: {factorial(k)}")
    
    print(round(result))
    return round(result)

number_of_groups(7, 4)