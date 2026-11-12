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

#Створює текстовийс файл, записує у нього підсумковий корінь і таблицю ходу ітерацій
def save_results_to_file(method_function) -> None:
    (root, iteretion_num, x_log) = method_function
    print(root, iteretion_num, x_log)
    result_file = open('results_variant_06.txt', 'w')

    result_file.write(f'Root of the function: {root:.7f}\n')
    result_file.write('\n\nIteration progress table:\n\n')
    result_file.write(f'{"Iteration number":<20}{"X value":<20}{"Function value":<20}{"Step value (|xn - xn-1|)"}\n')
    result_file.write(f'{0:<20}{x_log[0]:<20.4e}{target_function(x_log[0]):.4e}\n')
    for i in range(1, iteretion_num + 1):
        result_file.write(f'{i:<20}{x_log[i]:<20.4e}{target_function(x_log[i]):<20.4e}{abs(x_log[i]-x_log[i-1]):.4e}\n')
    
    result_file.close()


save_results_to_file(solve_newton(target_function, derivative_function, 100, 0.00008))
#print(solve_newton(target_function, derivative_function, 7, 0.00008))
