import example

def test_add():
    for i in range(10):
        for j in range(10):
            assert example.add(i, j) == i + j
