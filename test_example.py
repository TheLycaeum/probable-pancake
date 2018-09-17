import example

def test_sub():
    for i in range(10):
        for j in range(10):
            assert example.sub(i, j) == i - j
