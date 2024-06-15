class Data:
    def __init__(self):
        self.name = None
        self.age = None
        self.puls_results = []

    def write_data(self, data):
        self.puls_results.append(data)

    def calculate(self):
        result = (4 * sum(self.puls_results) - 200) / 10
        if 7 <= self.age <= 8:
            if result >= 21:
                return "Низький"
            elif 17 <= result <=20.9:
                return "Задовільний"
            elif 12 <= result <=16.9:
                return "Середній"
            elif 6.5 <= result <= 11.9:
                return "Вище середнього"
            elif 6.4 <= result:
                return "Високий"

        if 9 <= self.age <= 10:
            if result >= 19.5:
                return "Низький"
            elif 15.5 <= result <= 19.4:
                return "Задовільний"
            elif 10.5 <= result <= 15.4:
                return "Середній"
            elif 5 <= result <= 10.4:
                return "Вище середнього"
            elif 4.9<= result:
                return "Високий"

        if 11 <= self.age <= 12:
            if result >= 18:
                return "Низький"
            elif 14 <= result <= 17.9:
                return "Задовільний"
            elif 9 <= result <= 13.9:
                return "Середній"
            elif 3.5 <= result <= 8.9:
                return "Вище середнього"
            elif 3.4<= result:
                return "Високий"

        if 13 <= self.age <= 14:
            if result >= 16.5:
                return "Низький"
            elif 12.5 <= result <= 16.4:
                return "Задовільний"
            elif 7.5 <= result <= 12.4:
                return "Середній"
            elif 2 <= result <= 7.4:
                return "Вище середнього"
            elif 1.9<= result:
                return "Високий"

        if 15 >= self.age:
            if result >= 15:
                return "Низький"
            elif 11 <= result <= 14.9:
                return "Задовільний"
            elif 6 <= result <= 10.9:
                return "Середній"
            elif 0.5 <= result <= 5.9:
                return "Вище середнього"
            elif 0.4 <= result:
                return "Високий"

