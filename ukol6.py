from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calculate(self, *args):
        pass

class Sum(Operation):
    def calculate(self, *args):
        return sum(args)

class Multiply(Operation):
    def calculate(self, *args):
        if not args:
            return 0
        result = 1
        for num in args:
            result *= num
        return result

sum_obj = Sum()
res_sum = sum_obj.calculate(1, 3, 5, 0.1)
print(f"Výsledek sčítání (1 + 3 + 5 + 0.1): {res_sum}")

mul_obj = Multiply()
res_mul = mul_obj.calculate(1, 3, 5, 0.1)
print(f"Výsledek násobení (1 * 3 * 5 * 0.1): {res_mul}")