class Calculator(object):
    def __init__(self, starting_value: float = 0):
        """Starting value is zero"""
        self.__starting_value = starting_value

    def add(self, number=float) -> float:
        """Returns the sum of starting value (default: 0) plus provided number"""
        self.__starting_value += number
        return self.__starting_value

    def subtract(self, number=float) -> float:
        """Returns the difference of last starting value (default: 0) and provided number"""
        self.__starting_value -= number
        return self.__starting_value

    def multiply(self, number=float) -> float:
        """Returns the multiplication of last starting value (default: 0) by provided number"""
        self.__starting_value *= number
        return self.__starting_value

    def divide(self, number=float) -> float:
        """Return the division of last starting value (default: 0) by provided number"""
        try:
            self.__starting_value /= number
        except ZeroDivisionError:
            print("Division of zero is not possible")
        return self.__starting_value

    def nth_root(self, number=float) -> float:
        """Takes (n) root of last starting value. ((n)=number))
        :type number: float
        """
        result = self.__starting_value ** (1 / number)
        return result

    def reset(self) -> float:
        """ Resets starting value to 0"""
        return self.__starting_value == 0
