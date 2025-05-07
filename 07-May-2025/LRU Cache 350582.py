# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}
        self.left = None 
        self.right = None 

    def add_node_right(self, node):
        if not self.right:
            self.left = self.right = node
        else:
            self.right.next = node
            node.prev = self.right
            self.right = node

    def delete_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.left:
            self.left = node.next
        if node == self.right:
            self.right = node.prev

    def replace_node(self, node):
        self.delete_node(node)
        node.prev = node.next = None
        self.add_node_right(node)

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.replace_node(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.replace_node(node)
        else:
            node = Node(key, value)
            self.add_node_right(node)
            self.mp[key] = node
            if len(self.mp) > self.cap:
                lru = self.left
                self.delete_node(lru)
                del self.mp[lru.key]
