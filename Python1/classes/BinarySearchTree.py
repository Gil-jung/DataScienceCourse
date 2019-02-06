class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTreeSimple(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, node, key):
        if node is None or key == node.data:
            return node is not None
        elif key < node.data:
            return self._find_value(node.left, key)
        else:
            return self._find_value(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right   # 이해 필요
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)

    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def isLeftChild(self):
        return self.parent is not None and self.parent.leftChild is self

    def isRightChild(self):
        return self.parent is not None and self.parent.rightChild is self

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self.leftChild is None and self.rightChild is None

    def hasAnyChildren(self):
        return self.leftChild is not None or self.rightChild is not None

    def hasBothChildren(self):
        return self.leftChild is not None and self.rightChild is not None

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc

    def findSuccessor(self):
        succ = None
        if self.isLeaf():
            return succ
        elif self.hasRightChild():
            return self.rightChild.findMin()
        elif self.parent() is not None and self.hasLeftChild():
            return self.parent
        return succ

    def findMin(self):
        if self.hasLeftChild():
            return self.leftChild.findMin()
        else:
            return self

    def sliceOut(self):
        """ move node's child to its own position """
        if self.parent is not None and self.hasRightChild():
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
        # !!! the successor node never has a left child.

    def inorder_traverse(self):
        # ! in-order traverse prints out an sorted list.
        if self.hasLeftChild():
            self.leftChild.inorder_traverse()
        print(self.payload)
        if self.hasRightChild():
            self.rightChild.inorder_traverse()


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        if self.root is not None:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                currentNode.leftChild._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                currentNode.rightChild._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val)
        self.size += 1

    def get(self, key):
        if self.root is not None:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        return None

    def _get(self, key, currentNode):
        if currentNode is None:
            return None
        else:
            if key == currentNode.key:
                return currentNode
            elif key < currentNode.key:
                if currentNode.hasLeftChild():
                    currentNode.leftChild._get(key, currentNode.leftChild)
                else:
                    return None
            elif key > currentNode.key:
                if currentNode.hasRightChild():
                    currentNode.rightChild._get(key, currentNode.rightChild)
                else:
                    return None

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove is not None:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key is not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key is not in tree')

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.sliceOut()
            currentNode.key, currentNode.value = succ.key, succ.value
        else:
            child = currentNode.leftChild if currentNode.hasLeftChild() else currentNode.rightChild
            currentNode.leftChild = None
            currentNode.rightChild = None
            if currentNode.isRoot():
                self.root = child
            elif currentNode.isLeftChild():
                currentNode.parent.leftChild = child
            else:
                currentNode.parent.rightChild = child
        self.size -= 1





