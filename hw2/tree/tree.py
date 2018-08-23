class Tree(object):
    def __init__(self, root):
        """
        Constructor to initiate a tree object

        :param root:(Node) the root node of the tree
        """
        self.root = root

    '''
    def get_value_root(self):
        """
        Get the value of the root node

        :return:(int/str... or None) self.root.value or None
        """
        if self.root is not None:
            return self.root.value
        else:
            return None
    '''

    def get_tree_list(self, n):
        """
        Generate the tree in list form

        :param n:(Node) a node in the tree
        :return:(list) tree_list
        """
        if n.left is None and n.right is None:
            treelist = [str(n.value)]
        else:
            if n.left is None:
                left_branch = ["|"]
                right_branch = self.get_tree_list(n.right)
            elif n.right is None:
                left_branch = self.get_tree_list(n.left)
                right_branch = ["|"]
            else:
                left_branch = self.get_tree_list(n.left)
                right_branch = self.get_tree_list(n.right)
            if len(left_branch) > len(right_branch):
                if type(left_branch[0]) == str:
                    # left_width = 1
                    right_branch = ["|"]
                elif type(right_branch[0]) == str:
                    left_width = len(left_branch[0])
                    if type(right_branch[0]) == str:
                        right_width = 1
                    else:
                        right_width = len(right_branch[0])
                    width_delta = int((left_width - right_width) / 2)
                    right_branch = [["|"] * width_delta + [right_branch[0]] + ["|"] * width_delta]
                    delta_len = len(left_branch) - len(right_branch)
                    right_branch = right_branch + [["|"] * left_width] * delta_len
                else:
                    left_width = len(left_branch[0])
                    # if type(right_branch[0]) == str:
                    #     right_width = 1
                    # else:
                    #     right_width = len(right_branch[0])
                    # width_delta = int((left_width - right_width) / 2)
                    delta_len = len(left_branch) - len(right_branch)
                    for i in range(len(right_branch)):
                        lis = right_branch[i]
                        newlis = ["|"] * delta_len
                        for e in lis:
                            newlis = newlis + [e] + ["|"] * delta_len
                        right_branch[i] = newlis
                    right_branch = right_branch + [["|"] * left_width] * delta_len

            if len(right_branch) > len(left_branch):
                if type(right_branch[0]) == str:
                    # right_width = 1
                    left_branch = ["|"]
                elif type(left_branch[0]) == str:
                    right_width = len(right_branch[0])
                    if type(left_branch[0]) == str:
                        left_width = 1
                    else:
                        left_width = len(left_branch[0])
                    width_delta = int((right_width - left_width) / 2)
                    left_branch = [["|"] * width_delta + [left_branch[0]] + ["|"] * width_delta]
                    delta_len = len(right_branch) - len(left_branch)
                    left_branch = left_branch + [["|"] * right_width] * delta_len
                else:
                    right_width = len(right_branch[0])
                    # if type(left_branch[0]) == str:
                    #     left_width = 1
                    # else:
                    #     left_width = len(left_branch[0])
                    # width_delta = int((right_width - left_width) / 2)
                    delta_len = len(right_branch) - len(left_branch)
                    for i in range(len(left_branch)):
                        lis = left_branch[i]
                        newlis = ["|"] * delta_len
                        for e in lis:
                            newlis = newlis + [e] + ["|"] * delta_len
                        left_branch[i] = newlis
                    left_branch = left_branch + [["|"] * right_width] * delta_len

            if type(left_branch[0]) == str:
                left_width = 1
            else:
                left_width = len(left_branch[0])
            if type(right_branch[0]) == str:
                right_width = 1
            else:
                right_width = len(right_branch[0])
            top = ["|"] * left_width + [str(n.value)] + ["|"] * right_width
            bottom = []
            for i in range(len(left_branch)):
                if type(left_branch[i]) == str and type(right_branch[i]) != str:
                    bottom.append([left_branch[i]] + ["|"] + right_branch[i])
                elif type(left_branch[i]) != str and type(right_branch[i]) == str:
                    bottom.append(left_branch[i] + ["|"] + [right_branch[i]])

                elif type(left_branch[i]) == str and type(right_branch[i]) == str:
                    bottom.append([left_branch[i]] + ["|"] + [right_branch[i]])
                else:
                    bottom.append(left_branch[i] + ["|"] + right_branch[i])

            treelist = [top] + bottom

        return treelist

    '''
    def print_tree(self):
        """
        Process to print the tree in a user friendly form

        :return: None
        """
        treelist = self.get_tree_list(self.root)
        for i in range(len(treelist)):
            print("\t".join(treelist[i]))
        return
    '''


class Node(object):
    def __init__(self, value, left, right):
        """
        Constructor to initiate a Node object

        :param value:(str/int/...) value of the node
        :param left:(Node) the left child node of this node
        :param right:(Node) the right child node of this node
        """
        self.value = value
        self.left = left
        self.right = right


'''
if __name__ == '__main__':
    a = Node(1, None, None)
    tree1 = Tree(a)
    print(tree1.get_tree_list(a))
    tree1.print_tree()

    a = Node(1, None, None)
    b = Node(2, None, None)
    c = Node(3, None, None)
    d = Node(4, None, None)
    e = Node(5, None, None)
    f = Node(6, None, None)
    g = Node(7, None, None)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    tree2 = Tree(a)
    print(tree2.get_tree_list(a))
    tree2.print_tree()

    a = Node(1, None, None)
    b = Node(2, None, None)
    c = Node(3, None, None)
    a.left = b
    b.left = c
    tree3 = Tree(a)
    print(tree3.get_tree_list(a))
    tree3.print_tree()

    a = Node(1, None, None)
    b = Node(2, None, None)
    c = Node(3, None, None)
    d = Node(4, None, None)
    e = Node(5, None, None)
    f = Node(6, None, None)
    g = Node(7, None, None)
    a.left = b
    a.right = c
    b.right = d
    d.left = e
    c.left = f
    c.right = g
    tree4 = Tree(a)
    print(tree4.get_tree_list(a))

    a = Node(1, None, None)
    b = Node(2, None, None)
    c = Node(3, None, None)
    d = Node(4, None, None)
    e = Node(5, None, None)
    f = Node(6, None, None)
    g = Node(7, None, None)
    h = Node(8, None, None)
    i = Node(9, None, None)
    j = Node(10, None, None)
    k = Node(11, None, None)
    a.left = b
    a.right = c
    b.right = d
    d.left = e
    c.left = f
    c.right = g
    g.left = h
    e.right = i
    b.left = j
    j.right = k
    tree4 = Tree(a)
    print(tree4.get_tree_list(a))


    tree4.print_tree()
'''
