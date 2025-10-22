# Лабораторная работа № 4

## Формулировка задания
Разработайте программу на языке Python, которая будет строить **бинарное дерево** (_дерево, в каждом узле которого может быть только два потомка_). Отображение результата в виде словаря (как базовый вариант решения задания). Далее исследовать другие структуры, в том числе доступные в модуле collections в качестве контейнеров для хранения структуры бинарного дерева. 

**Необходимо реализовать нерекурсивный вариант gen_bin_tree**  

Алгоритм построения дерева должен учитывать параметры, переданные в качестве аргументов функции. Пример:   

```Python
def gen_bin_tree(height=<number>, root=<number>, left_branch=lambda l_r: l_r, right_branch=lambda r_r: r_r):**

    pass
```

Если параметры были переданы, то используются они. В противном случае используются параметры, указанные в варианте.

Root = 9; height = 6, 
left_leaf = 2*root+1, right_leaf = 2*root-1

## Описание работы кода
1. gen_bin_tree(height=6, root=9)
	- Это **нерекурсивная** функция, которая создаёт **бинарное дерево** с использованием очереди.
		Параметры
		- height - высота дерева (количество уровней).
		- root - значение текущего узла (корня дерева на этом уровне).
		- left_branch - функция для вычисления значения левого потомка.
		- right_branch - функция для вычисления значения правого потомка.
		База:
		- Если height == 0, возвращаем None. Это значит, что дерева нет.
		- Если height == 1, возвращаем только корневой узел.
		Алгоритм:
		- Используется очередь (foo) для обхода узлов и построения дерева по уровням.
		- Для каждого узла из очереди:
			- Если текущий уровень меньше высоты дерева:
			- left_leaf = 2*root+1 - значение левого ребёнка.
			- right_leaf = 2*root-1 - значение правого ребёнка.
			- Создаются новые узлы-потомки.
			- Потомки добавляются в очередь для дальнейшей обработки.
		Возврат словаря:
		- Узел представлен как словарь:
			``` python
			{
			  'root': root,
			  'left': левое_поддерево,
			  'right': правое_поддерево
			}
			```

## Решение
```Python
def gen_bin_tree(height=6, root=9, left_branch=lambda x: 2*x+1, right_branch=lambda x: 2*x-1):
    if height == 0:
        '''
        если высота будет 0, то дерева нет
        '''
        return None
    tree = {'root': root, 'left': None, 'right': None}
    '''
    создали наш корневой узел дерева        
    '''
    if height == 1:
        return tree
    '''
    а вот если высота 1, то мы вернём только корень дерева
    '''
    foo = []
    foo.append((tree,1))
    while foo:
        node,level=foo.pop(0)
        '''
        берём 1 узел из очереди и его уровень
        '''
        if level<height:
            '''
            тут собственно мы проверяем, не достигли мы максимальной высоты, если нет, то создаём дальше потомков
            '''
            left_vetka=left_branch(node['root'])
            right_vetka=right_branch(node['root'])
            '''
            вычисляем значения для левого и правого потомка по заданным формулам
            '''
            left_node={'root':left_vetka, 'left': None, 'right': None}
            right_node = {'root': right_vetka, 'left': None, 'right': None}
            '''
            создаём новые узлы потомки
            '''
            node['left']=left_node
            node['right']=right_node
            '''
            здесь мы уже прикрепляем текущих потомков к нашему узлу
            '''
            foo.append((left_node,level+1))
            foo.append((right_node,level+1))
            '''
            в конце всего мы должны в нашу очередь добавить потомков для дальшей построения, при этом увеличиваем уровень на 1
            '''
    return tree
'''
возвращаем наше готовое дерево
'''
```

## Проверка
- Импортируется функция gen_bin_tree.
- Создаётся класс MyTestCase.
- В классе определены 8 тестовых методов, каждый проверяет работу функции на разных входных данных.
	- test_zero_height: проверяет, что для height=0 возвращается None.
	- test_one_height: проверяет дерево высотой 1 (только корень).
	- test_default_root: проверяет использование корня по умолчанию (9).
	- test_left_calc: проверяет, что для tree['left']['root'] возвращается 19.
	- test_right_calc: проверяет, что для tree['right']['root'] возвращается 17.
	- test_different_root: проверяет работу с пользовательским корнем.
	- test_leaves_none: проверяет, что листья дерева высотой 2 имеют пустых потомков.
	- test_custom_formula: проверяет работу с пользовательской функцией для левого потомка.
- В конце запускается тестовый раннер с помощью unittest.main(), чтобы выполнить тесты и вывести подробный результат.
```Python
import unittest
from laba4 import gen_bin_tree


class MyTestCase(unittest.TestCase):
    def test_zero_height(self):
        result = gen_bin_tree(height=0)
        self.assertIsNone(result)

    def test_one_height(self):
        result = gen_bin_tree(height=1, root=5)
        self.assertEqual(result['root'], 5)
        self.assertIsNone(result['left'])
        self.assertIsNone(result['right'])

    def test_default_root(self):
        result = gen_bin_tree()
        self.assertEqual(result['root'], 9)

    def test_left_calc(self):
        result = gen_bin_tree(height=2, root=9)
        self.assertEqual(result['left']['root'], 19)

    def test_right_calc(self):
        result = gen_bin_tree(height=2, root=9)
        self.assertEqual(result['right']['root'], 17)

    def test_different_root(self):
        result = gen_bin_tree(height=2, root=3)
        self.assertEqual(result['root'], 3)

    def test_leaves_none(self):
        result = gen_bin_tree(height=2, root=9)
        self.assertIsNone(result['left']['left'])

    def test_custom_formula(self):
        result = gen_bin_tree(height=2, root=10,
                              left_branch=lambda x: x + 1)
        self.assertEqual(result['left']['root'], 11)


if __name__ == '__main__':
    unittest.main()
```

## Информация о студенте
Стажков Д.А, ИВТ 2.1