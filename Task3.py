class Worker:

    def __init__(self, wage, bonus, name="", surname="", position=""):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname + " " + self.position

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


a = Position(20000, 10000, "Иван", "Иванович", "Босс")
print(a.get_full_name())
print(a.get_total_income())