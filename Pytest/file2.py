import pytest

def my_add(a, b):
    return a + b
def my_sub(a, b):
    return a - b

class TestAddNumbers:
    @pytest.mark.parametrize('a, b, expected', [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (2, -4, -2)
    ])    
    def test_add_numbers(self,a,b,expected):
        assert my_add(a, b) == expected

    def test_add_large_numbers(self):
        assert my_add(1000000, 2000000) == 3000000

    #@staticmethod
    @pytest.mark.skip(reason="Not needed for TestEverything")
    def test_add_negative_numbers(self):
        assert add_numbers(-1, -2) == -3

    #@staticmethod
    @pytest.mark.skip(reason="Not needed for TestEverything")
    def test_add_zero(self):
        assert add_numbers(0, 0) == 0