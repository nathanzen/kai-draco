class TextNumbers:
    def __init__(self, size=8):
        if size <= 8:
            SystemError(f"range {size} is too low")

        self.size = 2 ** size

    def decode(self, numbers):
        result = ""

        i = 0
        while True:
            quotient = numbers // self.size ** i
            if not quotient:
                break
            result = chr(quotient % self.size) + result
            i += 1

        return result

    def encode(self, string):
        return sum([(self.size ** index) * ord(string) for index, string in enumerate(reversed(string))])
