import timeit
import matplotlib.pyplot as plt

def fact_recursive(n):
    """ факториал числа n рекурсивно
    если n==0 или n==1, возвращает 1
    в противном случае возвращает n * fact_recursive(n-1)
    """
    if n==0 or n==1:
        return 1
    return n * fact_recursive(n-1)

def fact_iterative(n):
    """Вычисляет факториал числа n с помощью цикла
    использует цикл for от 2 до n, постепенно умножая числа
    """
    result=1
    for i in range(2, n+1):
        result*=i
    return result
memo_rec={}
def fact_recursive_memo(n):
    """Рекурсивное вычисление факториала с мемоизацией
    сохраняет уже найденные значения факториала в словаре memo_rec,
    чтобы не пересчитывать их повторно
    """
    if n in memo_rec:
        return memo_rec[n]
    if n==0 or n==1:
        memo_rec[n]=1
    else:
        memo_rec[n]=n * fact_recursive_memo(n-1)
    return memo_rec[n]

# кэш для мемоизации итеративной версии
memo_it={}

def fact_iterative_memo(n):
    """Итеративное вычисление факториала с мемоизацией
    хранит результаты в словаре memo_it, чтобы ускорить повторные вызовы
    """
    if n in memo_it:
        return memo_it[n]
    result=1
    for i in range(2, n+1):
        result*=i
    memo_it[n]=result
    return result

# тестирование времени выполнения
numbers=list(range(5, 500, 20))  # список входных данных n
repeats=5  # количество повторов каждого измерения

# списки для записи результатов
times_recursive=[]
times_iterative=[]
times_recursive_memo=[]
times_iterative_memo=[]

# измеряем время выполнения для каждого метода
for n in numbers:
    t_rec=timeit.timeit(lambda: fact_recursive(n), number=repeats)/repeats
    t_it=timeit.timeit(lambda: fact_iterative(n), number=repeats)/repeats
    t_rec_m=timeit.timeit(lambda: fact_recursive_memo(n), number=repeats)/repeats
    t_it_m=timeit.timeit(lambda: fact_iterative_memo(n), number=repeats)/repeats

    times_recursive.append(t_rec)
    times_iterative.append(t_it)
    times_recursive_memo.append(t_rec_m)
    times_iterative_memo.append(t_it_m)

# построение графика
plt.figure(figsize=(10,6))
plt.plot(numbers, times_recursive, 'r--', label='рекурсивная')
plt.plot(numbers, times_iterative, 'b-', label='итеративная')
plt.plot(numbers, times_recursive_memo, 'g-.', label='рекурсивная с мемоизацией')
plt.plot(numbers, times_iterative_memo, 'm:', label='итеративная с мемоизацией')
plt.xlabel('n')
plt.ylabel('время выполнения (сек)')
plt.title('сравнение времени вычисления факториала')
plt.legend()
plt.grid(True)
plt.show()
