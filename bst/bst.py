class Bst:
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self.root = self.insert_node(self.root, value)
        self.size += 1

    def insert_node(self, cur_node, value):
        if cur_node is None:
            return self.Node(value)
        elif cur_node.value <= value:
            cur_node.right = self.insert_node(cur_node.right, value)
        else:
            cur_node.left = self.insert_node(cur_node.left, value)
        return cur_node

    def remove(self, value):
        self.root = self.remove_node(self.root, value)
        self.size -= 1

    def remove_node(self, cur_node, value):
        if cur_node is None:
            return None
        elif cur_node.value < value:
            cur_node.right = self.remove_node(cur_node.right, value)
        elif cur_node.value > value:
            cur_node.left = self.remove_node(cur_node.left, value)
        else:
            if cur_node.left and cur_node.right:
                min_node = self.find_min(cur_node.right)
                cur_node.value = min_node.value
                cur_node.right = self.remove_node(cur_node.right, min_node.value)
            elif cur_node.left:
                cur_node.value = cur_node.left.value
                cur_node.right = cur_node.left.right
                cur_node.left = cur_node.left.left
            elif cur_node.right:
                cur_node.value = cur_node.right.value
                cur_node.left = cur_node.right.left
                cur_node.right = cur_node.right.right
            else:
                del cur_node
                return None
            return cur_node

    @staticmethod
    def find_min(cur_node):
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    def __len__(self):
        return self.size

    def __contains__(self, value):
        return self.search_node(self.root, value)

    def search_node(self, cur_node, value):
        while cur_node is not None:
            if cur_node.value == value:
                return True
            elif cur_node.value < value:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        return False

    def __str__(self):
        return self.print_tree(self.root, 0).rstrip()

    def print_tree(self, cur_node, level):
        if cur_node:
            line1 = self.print_tree(cur_node.right, level + 1)
            line2 = '{:>{width}}\n'.format(cur_node.value, width=level * 2 + 1)
            line3 = self.print_tree(cur_node.left, level + 1)
            return ''.join([line1, line2, line3])
        return ''


def main():
    tree = Bst()
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    tree.insert(2)
    print('len is ', len(tree))
    print(3 in tree) # True
    print(6 in tree) # False
    tree.remove(3)
    print('len is ', len(tree))
    print(3 in tree) # True
    print(tree)
    tree.remove(4)
    tree.remove(1)
    tree.remove(2)
    print('len is ', len(tree))


if __name__ == "__main__":
    main()
