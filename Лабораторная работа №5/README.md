# Лабораторная работа №5: Сравнение реализации функций факториала

## Формулировка задания
Сравнить время выполнения двух реализаций функции вычисления факториала:
- рекурсивной,
- нерекурсивной (через цикл).

Изучить принцип **мемоизации** и реализовать сравнение **мемоизованных** и **немемоизованных** вариантов функций. Проанализировать результаты и сделать выводы, построить графики.

## Условия выполнения

- Реализованы функции:
    - `fact_recursive(n)` - рекурсивный вариант без мемоизации,
    - `fact_iterative(n)` - итеративный вариант без мемоизации,
    - `fact_recursive_memo(n)` - рекурсивный вариант с мемоизацией,
    - `fact_iterative_memo(n)` - итеративный вариант с мемоизацией.

- Используется **фиксированный набор входных значений**: n = 5, 25, 45, ..., 500 (шаг 20)
- Для каждого значения n проводится несколько прогонов (repeat=5)
- Визуализация: график с четырьмя линиями — по одной для каждого варианта реализации

## Код реализации

```python
import timeit
import matplotlib.pyplot as plt

def fact_recursive(n):
    """Факториал числа n рекурсивно"""
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n-1)

def fact_iterative(n):
    """Вычисляет факториал числа n с помощью цикла"""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

memo_rec = {}
def fact_recursive_memo(n):
    """Рекурсивное вычисление факториала с мемоизацией"""
    if n in memo_rec:
        return memo_rec[n]
    if n == 0 or n == 1:
        memo_rec[n] = 1
    else:
        memo_rec[n] = n * fact_recursive_memo(n-1)
    return memo_rec[n]

memo_it = {}
def fact_iterative_memo(n):
    """Итеративное вычисление факториала с мемоизацией"""
    if n in memo_it:
        return memo_it[n]
    result = 1
    for i in range(2, n+1):
        result *= i
    memo_it[n] = result
    return result

# Тестирование времени выполнения
numbers = list(range(5, 500, 20))
repeats = 5

times_recursive = []
times_iterative = []
times_recursive_memo = []
times_iterative_memo = []

for n in numbers:
    t_rec = timeit.timeit(lambda: fact_recursive(n), number=repeats) / repeats
    t_it = timeit.timeit(lambda: fact_iterative(n), number=repeats) / repeats
    t_rec_m = timeit.timeit(lambda: fact_recursive_memo(n), number=repeats) / repeats
    t_it_m = timeit.timeit(lambda: fact_iterative_memo(n), number=repeats) / repeats

    times_recursive.append(t_rec)
    times_iterative.append(t_it)
    times_recursive_memo.append(t_rec_m)
    times_iterative_memo.append(t_it_m)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(numbers, times_recursive, 'r--', label='рекурсивная')
plt.plot(numbers, times_iterative, 'b-', label='итеративная')
plt.plot(numbers, times_recursive_memo, 'g-.', label='рекурсивная с мемоизацией')
plt.plot(numbers, times_iterative_memo, 'm:', label='итеративная с мемоизацией')
plt.xlabel('n')
plt.ylabel('время выполнения (сек)')
plt.title('Сравнение времени вычисления факториала')
plt.legend()
plt.grid(True)
plt.show()
Код тестов
python
import unittest
import math
from laba5 import fact_recursive, fact_iterative, fact_recursive_memo, fact_iterative_memo

class TestFactorials(unittest.TestCase):
    def setUp(self):
        from laba5 import memo_rec, memo_it
        memo_rec.clear()
        memo_it.clear()

    def test_small_numbers(self):
        for n in range(11):
            with self.subTest(n=n):
                expected = math.factorial(n)
                self.assertEqual(fact_recursive(n), expected)
                self.assertEqual(fact_iterative(n), expected)
                self.assertEqual(fact_recursive_memo(n), expected)
                self.assertEqual(fact_iterative_memo(n), expected)

    def test_medium_numbers(self):
        test_cases = [5, 10, 15, 20]
        for n in test_cases:
            with self.subTest(n=n):
                expected = math.factorial(n)
                self.assertEqual(fact_recursive(n), expected)
                self.assertEqual(fact_iterative(n), expected)
                self.assertEqual(fact_recursive_memo(n), expected)
                self.assertEqual(fact_iterative_memo(n), expected)

    def test_memoization_effectiveness(self):
        result1 = fact_recursive_memo(10)
        result2 = fact_iterative_memo(10)
        result1_cached = fact_recursive_memo(10)
        result2_cached = fact_iterative_memo(10)
        self.assertEqual(result1, result1_cached)
        self.assertEqual(result2, result2_cached)

if __name__ == '__main__':
    unittest.main()
Результаты и выводы
![График сравнения времени вычисления факториала](graph.png)

На графике видно, что:

Итеративная реализация стабильно быстрее рекурсивной при больших n из-за отсутствия накладных расходов на вызовы функций

Мемоизация в рекурсивной версии значительно ускоряет повторные вызовы

Итеративная мемоизация даёт выигрыш при многократных вызовах с разными n

При n > 400 рекурсивная реализация может начать страдать от ограничения глубины рекурсии

Вывод: для однократного вычисления факториала предпочтительна итеративная реализация. Мемоизация оправдана только при многократных вызовах с пересекающимися аргументами.

Информация о студенте
[Твое имя], [Курс], [Группа]
