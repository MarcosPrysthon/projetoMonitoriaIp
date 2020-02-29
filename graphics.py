class Graphics:

    def __init__(self):
        self.years = []
        self.doors = []
        self.final_nums = []
        self.engines = []

    def get_years(self):
        return self.years

    def get_doors(self):
        return self.doors

    def get_final_nums(self):
        return self.final_nums

    def get_engines(self):
        return self.engines

    def set_years(self, data):
        years = []

        for i in range(len(data)):
            if data[i] == 'ANO' or data[i] == "Ano":
                years.append(data[i + 1])
                years.append(data[i + 2])
                years.append(data[i + 3])

        counter = 0
        years_aux = []
        years_str = ''
        for i in range(len(years)):
            if i == 44:
                years_str += years[i]
                years_aux.append(years_str)
            if i % 3 == 0:
                if i != 0:
                    years_aux.append(years_str)
                years_str = ''
                counter += 1
            years_str += years[i]

        for i in range(len(years_aux)):
            years_aux[i] = int(years_aux[i][:4])

        self.years = years_aux

    def set_doors(self, data):
        doors = []

        for i in range(len(data)):
            if data[i] == 'PORTAS' or data[i] == 'Portas':
                doors.append(int(data[i + 1]))

        self.doors = doors

    def set_engines(self, data):
        engines = []

        for i in range(len(data)):
            if data[i] == 'Motor:' or data[i] == 'motor':
                engines.append(float(data[i + 1]))

        self.engines = engines

    def set_final_nums(self, data):
        final_nums = []

        for i in range(len(data)):
            if data[i] == 'placa:' or data[i] == 'placa':
                if len(data[i + 1]) == 1:
                    final_nums.append(int(data[i + 1]))
                else:
                    final_nums.append(int(data[i + 1][:1]))

        self.final_nums = final_nums
