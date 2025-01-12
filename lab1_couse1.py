import doctest

class car:
    def __init__(self, arg1: float, arg2: int, arg3: float):
        self.fuel=arg1
        self.mileage=arg2
        self.MaxFuel=arg3
        def CheckFuelTank(self):
            """
            Возвращает литры в бензобаке типа float
            """
        def ResetMileage(self):
            """"
            #Скручивает пробег у машины, тоесть приравнивает mileage к нулю
            """
        def Refuel(self):
            if self.fuel<self.MaxFuel:
                """
                #Заправка автомобиля если количество бензина (fuel)<(MaxFuel) 
                возвращает значение bool в зависимости от успеха операции
                """

class polytech:
    def __init__(self, arg1: int, arg2: int):
        self.CountStudents=arg1
        self.BankAccount=arg2
    def CheckCountStudents(self):
        """
        возвращает количество студентов, обучающихся в университете
        типа (int)
        """
    def MoneyTransf(self, money: float):
        """
        Осуществляет денежный перевод для оплаты образовательных услуг в университете
        Возвращает тип bool в зависимости от успеха операции
        """
class room:
    def __init__(self, arg1: float, arg2: int, arg3: int):
        self.AreaOfRoom=arg1
        self.CountRoommates=arg2
        self.MaxRoommates=arg3
    def GetArea(self):
        """
        Возвращает площадь комнаты типа float
        """
        return self.AreaOfRoom
    def addRoomMate(self, Man: str):
        if self.MaxRoommates>self.CountRoommates:

            """
            Проверяет возможность подселения человека в комнату и по возможности подселяет его и увеличивает  CountRoommates
            возвращает значение типа boolean в зависимости от успеха операции
            """

__name__="__main__"
if __name__ == "__main__":
    doctest.testfile("example.txt")