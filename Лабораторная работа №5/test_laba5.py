# tests.py
import unittest
import math
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from laba5 import fact_recursive, fact_iterative, fact_recursive_memo, fact_iterative_memo
class TestFactorials(unittest.TestCase):

    def setUp(self):
        """
        Сбрасываем кэши перед каждым тестом
        """
        # Импортируем глобальные словари для мемоизации и очищаем их
        from laba5 import memo_rec, memo_it
        memo_rec.clear()
        memo_it.clear()

    def test_small_numbers(self):
        """
        Проверка факториала для малых чисел 0-10
        """
        for n in range(11):  # от 0 до 10
            with self.subTest(n=n):
                expected = math.factorial(n)
                self.assertEqual(fact_recursive(n), expected, f"Рекурсивная ошибка для n={n}")
                self.assertEqual(fact_iterative(n), expected, f"Итеративная ошибка для n={n}")
                self.assertEqual(fact_recursive_memo(n), expected, f"Рекурсивная с мемоизацией ошибка для n={n}")
                self.assertEqual(fact_iterative_memo(n), expected, f"Итеративная с мемоизацией ошибка для n={n}")

    def test_medium_numbers(self):
        """
        Проверка факториала для средних чисел
        """
        test_cases = [5, 10, 15, 20]
        for n in test_cases:
            with self.subTest(n=n):
                expected = math.factorial(n)
                self.assertEqual(fact_recursive(n), expected)
                self.assertEqual(fact_iterative(n), expected)
                self.assertEqual(fact_recursive_memo(n), expected)
                self.assertEqual(fact_iterative_memo(n), expected)

    def test_zero_and_one(self):
        """
        Проверка базовых случаев 0! = 1 и 1! = 1
        """
        self.assertEqual(fact_recursive(0), 1)
        self.assertEqual(fact_iterative(0), 1)
        self.assertEqual(fact_recursive_memo(0), 1)
        self.assertEqual(fact_iterative_memo(0), 1)

        self.assertEqual(fact_recursive(1), 1)
        self.assertEqual(fact_iterative(1), 1)
        self.assertEqual(fact_recursive_memo(1), 1)
        self.assertEqual(fact_iterative_memo(1), 1)

    def test_memoization_effectiveness(self):
        """
        Проверка работы мемоизации
        """
        # Первый вызов
        result1 = fact_recursive_memo(10)
        result2 = fact_iterative_memo(10)

        # Второй вызов - должен использовать кэш
        result1_cached = fact_recursive_memo(10)
        result2_cached = fact_iterative_memo(10)

        self.assertEqual(result1, result1_cached)
        self.assertEqual(result2, result2_cached)

    def test_consistency_between_methods(self):
        """
        Проверка согласованности между разными методами
        """
        test_numbers = [0, 1, 5, 10, 15]

        for n in test_numbers:
            with self.subTest(n=n):
                recursive = fact_recursive(n)
                iterative = fact_iterative(n)
                recursive_memo = fact_recursive_memo(n)
                iterative_memo = fact_iterative_memo(n)

                # Все методы должны давать одинаковый результат
                self.assertEqual(recursive, iterative)
                self.assertEqual(iterative, recursive_memo)
                self.assertEqual(recursive_memo, iterative_memo)

                # И соответствовать математическому факториалу
                self.assertEqual(recursive, math.factorial(n))


def run_tests():
    """
    Запуск тестов с подробным выводом
    """
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFactorials)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == '__main__':
    print("Запуск тестов для функций факториала")
    success = run_tests()

    if success:
        print("\n Все тесты прошли успешно!")
    else:
        print("\n Некоторые тесты не прошли")

    # Демонстрация работы всех методов
    print(f"\nПроверка вычисления 10! разными методами:")
    print(f"math.factorial(10) = {math.factorial(10)}")
    print(f"fact_recursive(10) = {fact_recursive(10)}")
    print(f"fact_iterative(10) = {fact_iterative(10)}")
    print(f"fact_recursive_memo(10) = {fact_recursive_memo(10)}")
    print(f"fact_iterative_memo(10) = {fact_iterative_memo(10)}")