def mergeLists(head1, head2):
    my_list = []
    node = head1
    while node is not None:
        my_list.append(node.data)
        node = node.next
    node2 = head2
    while node2 is not None:
        my_list.append(node2.data)
        node2 = node2.next
    my_list.sort()
    
    ll3 = SinglyLinkedList()
    for num in my_list:
        ll3.insert_node(num)
        
    return ll3.head
