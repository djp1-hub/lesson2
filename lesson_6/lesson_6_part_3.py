class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    me = Position('Gennady', 'Leonov', 'Head of IT', 300, 100)
    him = Position('Sidorov', 'Vladimir', 'CTO', 350, 120)
    print(me.get_full_name())
    print(f'Total income: {me.get_total_income()}')
    print(me._income)
    print(him.get_full_name())
    print(f'Total income: {him.get_total_income()}')
    print(him.position)