# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def has_cycle(self, graph, cur_node, visited, result):
        if visited[cur_node] == 1:
            return False
        if visited[cur_node] == 2:
            return True
        visited[cur_node] = 2
        for next_node in graph[cur_node]:
            if self.has_cycle(graph, next_node, visited, result):
                return True
        visited[cur_node] = 1
        result.append(cur_node)
        return False

    def sortItems(self, n: int, m: int, group: List[int],
                  beforeItems: List[List[int]]) -> List[int]:
        group_items_map = defaultdict(list)
        visited_item = defaultdict(dict)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group_items_map[group[i]].append(i)
            visited_item[group[i]][i] = 0

        graph_group = defaultdict(set)
        graph_item = {i: defaultdict(list) for i in range(m)}

        for item_after, before_items in enumerate(beforeItems):
            for item_before in before_items:
                group_before = group[item_before]
                group_after = group[item_after]

                if group_before != group_after:
                    graph_group[group_before].add(group_after)
                else:
                    graph_item[group_before][item_before].append(item_after)
        visited_group = [0] * m
        group_order = []
        for group_id in range(m):
            if self.has_cycle(graph_group, group_id,
                              visited_group, group_order):
                return []

        full_item_order = []
        for group_id in group_order:
            for item_id in group_items_map[group_id]:
                if self.has_cycle(graph_item[group_id], item_id,
                                  visited_item[group_id], full_item_order):
                    return []
        return full_item_order[::-1]