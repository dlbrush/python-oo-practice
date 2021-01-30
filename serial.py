"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes
    __________
    start: The number that will be generated first. Further numbers will count up from this value.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """
        Create a serial number generator that will generate incrementing numbers 
        starting from a passed value
        """
        self.start = start
        self.count = start

    def __repr__(self):
        return f"<SerialGenerator Start={self.start} Next number:{self.count}>"

    def generate(self):
        "Generate a unique serial number. Should be 1 value higher than the last number generated."
        val = self.count
        self.count += 1
        return val

    def reset(self):
        "Reset the count so that the next number generated will return to the start value."
        self.count = self.start

        

