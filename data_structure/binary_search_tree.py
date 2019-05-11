# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-04-07 16:06:28
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-04-07 20:23:44

from typing import List


if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from data_structure.binary_tree import BinaryTree
else:
    from data_structure.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    class ContentNode(BinaryTree.Node):
        """node with content"""

        def __init__(self, key, content):
            super().__init__(key)
            self.key = key
            self.content = [content]

    def __init__(self, key=None, content=None):
        if key is None:
            self.root = None
        else:
            self.root = BinarySearchTree.ContentNode(key, content)

    def search(self, key: int) -> List:
        n = self.root
        while n:
            if n.key == key:
                return n.content
            elif key < n.key:
                n = n.left
            else:
                n = n.right
        else:
            return []

    def insert(self, key, content):
        if self.root is None:
            self.root = BinarySearchTree.ContentNode(key, content)
            return

        n = self.root
        while n:
            if n.key == key:
                n.content.append(content)
                return
            elif key < n.key:
                if n.left is None:
                    n.left = BinarySearchTree.ContentNode(key, content)
                    return
                else:
                    n = n.left
                    continue
            else:
                if n.right is None:
                    n.right = BinarySearchTree.ContentNode(key, content)
                    return
                else:
                    n = n.right
                    continue

    def delete(self, key, content=None) -> bool:
        n = self.root
        while n:
            if n.key == key:
                if content is None:
                    n.content.clear()
                    return True
                else:
                    n.content.remove(content)
                    return True
            elif key < n.key:
                n = n.left
            else:
                n = n.right
        else:
            return False

    def ceiling(self, key):
        n = self.root
        result = None
        while n:
            if n.key == key and n.content:
                return n
            elif key < n.key:
                if n.content:
                    result = n
                n = n.left
            else:
                n = n.right
        return result

    def floor(self, key):
        n = self.root
        result = None
        while n:
            if n.key == key and n.content:
                return n
            elif key < n.key:
                n = n.left
            else:
                if n.content:
                    result = n
                n = n.right
        return result


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(5, 5)
    bst.insert(7, 7)
    bst.insert(3, 3)
    bst.insert(6, 6)

    print("tree structure")
    queue = [bst.root]
    while queue:
        data = []
        for _ in range(len(queue)):
            n = queue.pop(0)
            data.append(str(n.key))
            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)
        print(" ".join(data))

    print("search 3", bst.search(3))
    print("ceiling 4", bst.ceiling(4).value)
    print("floor 4", bst.floor(4).value)
    print("delete 3")
    bst.delete(3)
    print("search 3", bst.search(3))
    print("ceiling 4", bst.ceiling(4).value)
    print("floor 4", bst.floor(4).value)
