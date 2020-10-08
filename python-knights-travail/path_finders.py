from tree import Node
from collections import deque
class KnightPathFinder:
    def __init__(self,coordinates):
        self._x, self._y = coordinates
        self._root = Node(coordinates)
        self._considered_positions = {coordinates,}

    @property
    def considered_positions(self):
        return self._considered_positions

    @property
    def root(self):
        return self._root

    def get_valid_moves(self, pos):
        x,y = pos
        valid_moves = set()
        moves = {
            (x+1,y+2),
            (x+1,y-2),
            (x-1,y+2),
            (x-1,y-2),
            (x+2,y+1),
            (x+2,y-1),
            (x-2,y+1),
            (x-2,y-1),
        }
        for move in moves:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                valid_moves.add(move)
        return valid_moves

    def new_move_positions(self,pos):
        valid_moves = self.get_valid_moves(pos)
        new_positions = valid_moves - self.considered_positions
        self.considered_positions.update(new_positions)
        return new_positions

    def build_move_tree(self):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            children = self.new_move_positions(node.value)
            for child in children:
                ch_node = Node(child)
                node.add_child(ch_node)
                queue.append(ch_node)

    def find_path(self, end_position):
        end_node = self.root.depth_search(end_position)
        return self.trace_to_root(end_node)

    def trace_to_root(self, end_node):
        path = []
        node = end_node
        while node:
            path.append(node.value)
            node = node.parent
        return path[::-1]


# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
# print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
# print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
# print(finder.find_path((7, 6)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
