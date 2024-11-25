#OOP Concepts

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # def append(self, value):
    #     new_node = Node(value)
    #     if not self.head:
    #         self.head = new_node
    #         self.tail = new_node
    #         return True
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next
    #     temp.next = new_node
    #     self.tail = new_node
    #     self.length += 1
    #     return True

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True # Optional

    # def pop(self):
    #     if not self.head: # If list is empty
    #         return None
    #     temp = self.head
    #     if not temp.next: # If there is only one node
    #         value = temp.value
    #         self.head = value # Reset head to none
    #         return value
    #     pre = self.head
    #     while temp.next: # TRaverse to the last node
    #         pre = temp
    #         temp = temp.next
    #     pre.next = None # Remove the last node
    #     self.length -= 1
    #     return temp.value # Return value of the popped node

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def display_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="=>")
            temp = temp.next
        print("None")

    
    def prepend_item(self, value):
        #initialize new value
        #if list is empty, self.head = new_value
        #if not empty assign self.head to temp variable
        #assign self.head new_value
        #self.next = temp
        new_value = Node(value)
        if not self.head:
            self.head = new_value
            return True
        else:
            new_value.next = self.head
            self.head = new_value
        self.length += 1
        return True

    def pop_first(self):
        #if list empty return none
        #if list only one node, set self.head to None
        #if list more than 1, assign temp to self.head
        #self.head = self.next

        if self.head is None:
            return None
        temp = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return temp.value

    def get(self, index):
        # check index is within list
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        current_node = self.get(index)
        if current_node:
            current_node.value = value
            return True
        return False

    def insert_value(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0: # if index is at the start of the list
            return self.prepend_item(value)
        if index == self.length: # end of the list
            return self.append(value)
        # a > b > c > null
        new_value = Node(value)
        prev_node = self.get(index-1) # get previous node
        temp = prev_node.next
        prev_node.next = new_value
        new_value.next = temp
        self.length += 1
        return True

    def remove(self,index):
        # check if index exist
        if index < 0 or index > self.length:
            return None
        # if index is 0 use pop_first
        if index == 0:
            return self.pop_first()
        if index == self.length: # if index equals length i.e end of list use pop
            return self.pop()
        prev_node = self.get(index - 1)
        temp = prev_node.next
        prev_node.next = temp.next
        temp.next = None # removes from list
        self.length -= 1
        return temp

    def reverse(self):
        """
            (head)1 > 2 > 5 > 8 > (tail)3 > None
            define a temp value assign self.head
            temp = self.head
            asign self.head = self.tail
            self.head = self.tail
            assign self.tail = temp
            self.tail = temp
            to reverse the remaining nodes
            2 > 5 > 8
            assign a temp value to hold the current node
            after_next_node = temp.next
            before_temp = None # point to none
            iterate through the items and reverse the pointers
            after_next_node = temp.next [5]
            temp.next = before_temp [2 < 5_8] reverses pointer
            before_temp = temp []
            temp = after_next_node
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after_next_node = temp.next
        before_temp = None # point to none
        for _ in range(self.length):
            after_next_node = temp.next
            temp.next = before_temp
            before_temp = temp
            temp = after_next_node

        
    # def find_middle_node(self):
    #     if not self.head:
    #         return None
    #     slow_pointer = 0
    #     fast_pointer = 0
    #     current_node = self.head
    #     next_node = self.head.next
    #     after_next_node = next_node.next
    #     while after_next_node:
    #         current_node = next_node
    #         next_node = current_node.next

    #         temp = after_next_node
    #         temp_after = temp.next
    #         after_next_node = temp_after.next
    #         slow_pointer += 1
    #         fast_pointer += 2
    #     return slow_pointer
        
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    

def find_kth_from_end(ll, k):
    slow = fast = ll.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
        
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow.value



ll = LinkedList()
ll.display_list()
ll.append(8)
ll.display_list()
ll.append(100)
ll.display_list()
ll.prepend_item(16)
ll.display_list()
ll.append(900)
ll.display_list()
ll.pop()
ll.display_list()
ll.pop_first()
ll.display_list()
ll.append(99)
ll.display_list()
# ll.prepend_item(32)
# ll.display_list()
print(ll.get(2))
ll.set_value(0,500)
ll.display_list()
ll.insert_value(1,78)
ll.display_list()
ll.insert_value(3,59)
ll.display_list()
ll.insert_value(3,65)
ll.display_list()
# ll.remove(2)
# ll.display_list()
# ll.reverse()
# ll.display_list()

print(ll.find_middle_node())

print(find_kth_from_end(ll, 2))