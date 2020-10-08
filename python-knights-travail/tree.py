from collections import deque
class Node:
    
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value
    
    @property
    def children(self):
        return self._children

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            if child.parent != self:
                child.parent = self

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self,parent):
        if self.parent:
            self.parent.remove_child(self)
        if parent:
            self._parent = parent
            parent.add_child(self)
        else:
            self._parent = None

    def depth_search(self, value):
        if self.value == value:
            return self
        for node in self.children:
            res = node.depth_search(value)
            if res:
                return res
        return None

    def breadth_search(self, value):
        queue = deque([self])
        while len(queue) > 0:
            node = queue.popleft()
            if node.value == value:
                return node
            queue.extend(node.children)
        return None


# node1 = Node("node1")
# node2 = Node("node2")
# node3 = Node("node3")

# node2.parent = node3
# print(node2.parent)
