from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 4, 5) == 9

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(self, 15, 3) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 4, 3) == 1

    def teardown(self):
        print('Завершение таста')