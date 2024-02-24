class Date:
    def __init__(self, year = 1, month = 1, day = 1):
        self.year = year
        self.month = month
        self.day = day
        if not self.validate():
            raise ValueError ( "Invalid date")


    def input_date(self):
        year, month, day = map(int, input("Введите дату ГГГГ.ММ.ДД: ").split('.'))
        self.year = year
        self.month = month
        self.day = day
        if not self.validate():
            raise ValueError ("Invalid date")

    def __str__(self):
        return f"{self.year}.{self.month}.{self.day}"
        
    def validate(self):
        if self.year < 1 or self.month < 1 or self.month > 12 or self.day < 1:
            return False
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            maxday = 31
        elif self.month in [4, 6, 9, 11]:
            maxday = 30
        else:
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                maxday = 29
            else:
                maxday = 28
        if self.day > maxday:
            return False 
        return True



