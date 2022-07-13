from utils.listnode import ListNode
from utils import listnode

l1 = [1,2,3,4,5,6]
list1 = listnode.list_to_LL(l1)

def middle(head):
    values = []
    my_list = head
    while my_list:
        values.append(my_list.val)
        my_list = my_list.next
    ll_length = len(values)
    for i in range(0, ll_length // 2):
        head = head.next
    return head

print(middle(list1))