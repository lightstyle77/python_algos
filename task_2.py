"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # Валидация узлов с требованиями для бинарного дерева
        # if new_node > self.root:
        #     raise ValueError(f'Значение должно быть меньше {self.root}')
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            if new_node > self.root:
                raise ValueError(f'Значение должно быть меньше {self.root}')
            else:
                self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # Валидация узлов с требованиями для бинарного дерева

        # если у узла нет правого потомка
        if self.right_child is None:
            if new_node < self.root:
                raise ValueError(f'Значение должно быть больше {self.root}')
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            else:
                self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


if __name__ == '__main__':
    r = BinaryTree(10)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(5)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right(14)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(32)
    print(r.get_right_child().get_root_val())
