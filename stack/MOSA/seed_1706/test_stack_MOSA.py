#Pyguin test cases converted from stack/MOSA/seed_1706/test_stack.py
import stack as module_0
import linked_list2 as module_1

def test_case_0():
    stack_0 = module_0.Stack()

def test_case_1():
    none_type_0 = None
    stack_0 = module_0.Stack(none_type_0)
    var_0 = stack_0.push(none_type_0)
    stack_1 = module_0.Stack()
    linked_list_0 = module_1.LinkedList()
    var_1 = linked_list_0.push(none_type_0)
    var_1.pop()

def test_case_2():
    stack_0 = module_0.Stack()
    stack_0.pop()
