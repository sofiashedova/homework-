class Date:
    def __init__(self, year = 1, month = 1, day = 1):
        self.year = year
        self.month = month
        self.day = day

    def input_date(self):
        year, month, day = map(int, input("Введите дату ГГГГ.ММ.ДД: ").split('.'))
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}.{self.month}.{self.day}"
        
    



