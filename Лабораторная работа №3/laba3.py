def gen_bin_tree(height=6, root=9):
    """
    Создаём функцию, которая создаёт бинарное дерево
    :param height: это как бы высота нашего дерево, то есть количество уровней
    :param root: это уже значение в корне дерева, ну как бы самый верхний узел
    :return:
    """
    # При условии, что высота =1
    if height == 1:
        # если да, то будем считать левого и правого потомка по формулам
        left = root * 2 + 1
        right = 2 * root - 1
        # возвращаем словарь в которых входит корень, левый и правый
        return {str(root): [str(left), str(right)]}
    # тут создаём левое поддерево, но на высоту на 1 меньше
    left_tree = gen_bin_tree(height - 1, root * 2 + 1)
    # следовательно и правую также, на высоту меньше
    right_tree = gen_bin_tree(height - 1, 2 * root - 1)
    return {str(root): [left_tree, right_tree]}
result = gen_bin_tree(2, 9)
