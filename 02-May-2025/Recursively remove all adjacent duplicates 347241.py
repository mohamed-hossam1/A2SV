# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

def remove_adjacent_duplicates(s):
    def remove_once(s):
        result = []
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                # Skip all adjacent duplicates
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                i += 1  # Skip the last one in the group
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)

    prev = None
    while prev != s:
        prev = s
        s = remove_once(s)
    return s