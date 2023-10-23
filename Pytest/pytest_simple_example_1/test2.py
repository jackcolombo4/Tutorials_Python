import pytest

def add_numbers(a, b):
    return a + b
def subtract(a, b):
    return a - b


class TestAddNumbers:
    @pytest.mark.parametrize('a, b, expected', [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (2, -4, -2)
    ])
    def test_add_numbers(self, a, b, expected):
        print("ale")
        assert add_numbers(a, b) == expected

    def test_add_numbers_with_large_numbers(self):
        assert add_numbers(1000000, 2000000) == 3000000

    def test_numbers4(self):
        assert subtract(4, 3) == 1

    def test_numbers2(self):
        assert subtract(4, 3) == 1

"""    
if __name__ == '__main__':
    a = TestAddNumbers()
    a.test_add_numbers_with_large_numbers2()
"""