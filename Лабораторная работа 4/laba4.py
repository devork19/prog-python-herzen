def gen_bin_tree(height=6,root=9, left_branch= lambda x: 2*x+1, right_branch= lambda x:2*x-1):
    if height==0:
        '''
        если высота будет 0, то дерева нет
        '''
        return None
    tree = {'root': root, 'left': None, 'right': None}
    '''
    создали наш корневой узел дерева        
    '''
    if height==1:
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

