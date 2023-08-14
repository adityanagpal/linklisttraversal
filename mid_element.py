########### LinkedList Abstract Data Type ##################

class LinkedList:
    def __init__(self,val=None):
        self.val = val
        self.next = None


###########  Creating some Test Data ##########
l1 = [i for i in range(11)]
l2 = [i*2 for i in range(5)]
l3 = [i+3 for i in range(7)]

def create_linked_list(list_values):
    head_node = LinkedList()
    temp_node = head_node
    for element in list_values:
        temp_node.next = LinkedList(element)
        temp_node = temp_node.next
    return head_node.next
h1 = create_linked_list(l1)
h2 = create_linked_list(l2)
h3 = create_linked_list(l3)

############## write the function to get mid element ###########

def mid_element(node):
    fast_pointer = node
    slow_pointer = node
    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
    return slow_pointer.val

print(l1,'----',mid_element(h1),'-----',mid_element(h1)==l1[len(l1)//2])
print(l2,'----',mid_element(h2),'-----',mid_element(h2)==l2[len(l2)//2])
print(l3,'----',mid_element(h3),'-----',mid_element(h3)==l3[len(l3)//2])
