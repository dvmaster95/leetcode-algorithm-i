from utils.listnode import ListNode
from utils import listnode

l1 = [1,2]
list1 = listnode.list_to_LL(l1)

def middle(head, n):
    def list_to_LL(arr):
        if len(arr) < 1:
            return []
        if len(arr) == 1:
            return ListNode(arr[0])
        return ListNode(arr[0], next=list_to_LL(arr[1:]))
    values = []
    my_list = head
    while my_list:
        values.append(my_list.val)
        my_list = my_list.next
    if n == 1:
        values.pop()
    else:
        values = values[:-n] + values[-n+1:]
    return list_to_LL(values)

print(middle(list1, 1))