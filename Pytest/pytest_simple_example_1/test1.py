from test2 import TestAddNumbers

@pytest.mark.test_vari
class TestEverything:
#     def test_add_numbers_wrap(self):
#         TestAddNumbers().test_add_numbers(1,2,3)
# 
#     def test_add_numbers_wrap_with_large_numbers(self):
#         TestAddNumbers().test_add_numbers_with_large_numbers()
    
    def test_add_numbers_with_negative_numbers(self):
        test = TestAddNumbers()
        a, b, expected = -1, -2, -3
        test.test_add_numbers(a, b, expected)