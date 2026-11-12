"""
Лабораторна робота: №5 Функції та декомпозиція задач
Варіант: 6
Студент: Поліщук Віктор
Група: EIP30 Група 2
"""
import math

#Функція для якої ми шукаємо корінь
def target_function(x: float) -> float:
    return 2*x**2 - x**4 - 1 - math.log(x)

#Аналітично знайдена похідна для заданої функції
def derivative_function(x: float) -> float:
    return 4*x - 4*x**3 - 1/x

#Функція для пошуку кореня рівняння Методом Ньютона (дотичних)
def solve_newton(f, df, x0: float, eps: float) -> tuple: 
    x = []  
    x.append(x0)
    x.append(x0 - f(x0)/df(x0))
    iter_cnt = 1
    while abs(x[iter_cnt] - x[iter_cnt - 1]) >= eps:
        x.append(x[iter_cnt] - f(x[iter_cnt])/df(x[iter_cnt]))
        iter_cnt += 1

    return (x[iter_cnt], iter_cnt, x)

print(solve_newton(target_function, derivative_function, 7, 0.00008))
