"""
Goal of the program: A PrimeIterator class
by Fran Ogallas
Start: 13th of May 2024. Last update: 13th of May 2024
"""
from collections.abc import Iterator


class PrimeIterator(Iterator):
    def __init__(self, max_number: int):
        self.__max_number = max_number
        self.n = 0

    def __next__(self):
        next_prime = self.__find_next_prime(self.n)
        if next_prime > self.__max_number:
            raise StopIteration
        self.n = next_prime
        return self.n

    def __is_prime(self, number):
        if number - int(number) != 0:
            raise ValueError("is_prime function cannot receive floating numbers.")
        if number < 2:
            return False
        elif number == 2:
            return True
        else:
            half = round(number / 2)
            prime_detection = True
            counter = 2
            while prime_detection and counter <= half:
                tested_number = number / counter
                if tested_number - int(tested_number) == 0:
                    prime_detection = False
                counter += 1
            return prime_detection

    def __find_next_prime(self, number):
        result = number
        while True:
            result += 1
            if self.__is_prime(result):
                return result


def main():
    custom_iterator = PrimeIterator(100)
    print(list(custom_iterator))


if __name__ == "__main__":
    main()
