import pytest
from priority_queue1 import PriorityQueue


def test_pq_simple():
    pq = PriorityQueue()
    pq.add_task('drive to work', 2)
    pq.add_task('get keys')
    pq.add_task('load car', 1)
    pq.add_task('check gas', 1)
    pq.add_task('turn on car', 1)
    pq.add_task('park at work', 3)
    pq.remove_task('load car')
    pq.add_task('check gas', 1)

    assert pq.pop_task() == 'get keys'
    assert pq.pop_task() == 'turn on car'
    assert pq.pop_task() == 'check gas'
    assert pq.pop_task() == 'drive to work'
    assert pq.pop_task() == 'park at work'

    with pytest.raises(KeyError):
        pq.pop_task()


def test_set_priority():
    pq = PriorityQueue()
    pq.add_task('drive to work', 2)
    pq.add_task('get keys')
    pq.add_task('load car', 1)
    pq.add_task('check gas', 1)
    pq.add_task('turn on car', 1)
    pq.add_task('park at work', 3)
    pq.remove_task('load car')
    pq.add_task('check gas', 1)

    assert pq.pop_task() == 'get keys'

    pq.set_priority('park at work', 0)

    assert pq.pop_task() == 'park at work'

    pq.set_priority('load car', 5)

    assert pq.pop_task() == 'turn on car'

