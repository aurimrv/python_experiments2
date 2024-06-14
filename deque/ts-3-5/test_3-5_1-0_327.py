import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from deque import Deque

@pytest.fixture
def deque_setup():
    deque = Deque()
    return deque

def test_append(deque_setup):
    deque_setup.append(1)
    assert deque_setup._container.head.data == 1

def test_append_multiple_values(deque_setup):
    deque_setup.append(3)
    deque_setup.append(5)
    assert deque_setup._container.tail.data == 5

def test_appendleft(deque_setup):
    deque_setup.appendleft(7)
    assert deque_setup._container.tail.data == 7

def test_appendleft_multiple_values(deque_setup):
    deque_setup.appendleft(2)
    deque_setup.appendleft(4)
    assert deque_setup._container.head.data == 4

def test_pop(deque_setup):
    deque_setup.append(10)
    result = deque_setup.pop()
    assert result == 10

def test_pop_empty(deque_setup):
    with pytest.raises(Exception):
        deque_setup.pop()

def test_popleft(deque_setup):
    deque_setup.append(20)
    result = deque_setup.popleft()
    assert result == 20

def test_popleft_empty(deque_setup):
    with pytest.raises(Exception):
        deque_setup.popleft()

def test_peek(deque_setup):
    deque_setup.append(30)
    result = deque_setup.peek()
    assert result == 30

def test_peek_empty(deque_setup):
    result = deque_setup.peek()
    assert result == None

def test_peekleft(deque_setup):
    deque_setup.append(40)
    result = deque_setup.peekleft()
    assert result == 40

def test_peekleft_empty(deque_setup):
    result = deque_setup.peekleft()
    assert result == None

def test_size_empty(deque_setup):
    assert deque_setup.size() == 0

def test_size_nonempty(deque_setup):
    deque_setup.append(50)
    deque_setup.append(60)
    assert deque_setup.size() == 2