# Problem: Delete a linked list using recursion - https://www.geeksforgeeks.org/delete-linked-list-using-recursion/

def delete_list(cur):
    if cur is None:
        return

    delete_list(cur.next)
    curr = None