class calculate:
    def __init__(self, first_number, second_number):

            self.first_numbeer = first_number
            self.second_number = second_number



    def add(self):
        return self.first_numbeer + self.second_number

    def mul(self):
        return self.first_numbeer * self.second_number

    def sub(self):
        return self.first_numbeer - self.second_number

    def div(self):
        if self.second_number != 0:
            return self.first_numbeer / self.second_number
        else:
            return f'Division by zero is invalid...'
