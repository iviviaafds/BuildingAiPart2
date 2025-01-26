import doctest

#Создает объект типа машина. На вход подаются такие аргументы как
#Уровень топлива в бензобаке в литрах, тип float
#Пробег в км, тип int
#Максимальный объем бака в литрах, тип float
class Car:
    def __init__(self, arg1: float, arg2: int, arg3: float):
        self.fuel=arg1
        self.mileage=arg2
        self.MaxFuel=arg3
    def CheckFuelTank(self):
        """
        Возвращает литры в бензобаке типа float
        Пример вызова
        fuel=car.CheckFuelTank()
        """
    def ResetMileage(self):
        """"
        #Скручивает пробег у машины, то есть приравнивает mileage к нулю
        Пример вызова
        car.ResetMileage()
        """
    def Refuel(self):
        if self.fuel<self.MaxFuel:
            """
            #Заправка автомобиля если количество бензина (fuel)<(MaxFuel) 
            возвращает значение bool в зависимости от успеха операции
            Пример инициализации
            car.Refuel()
            """
#Пример инициализации
#Skoda = Car(30, 200000, 80)



#Создает объект типа Политех На вход подаются такие аргументы как
#Количество студентов, обучающихся в университете, тип int
#Банковский счет Политеха, тип int
class Polytech:
    def __init__(self, arg1: int, arg2: int):
        self.CountStudents=arg1
        self.BankAccount=arg2
    def CheckCountStudents(self):
        """
        возвращает количество студентов, обучающихся в университете
        типа (int)
        Пример вызова
        Count=poly.CountStudents()
        """
    def MoneyTransf(self, money: float):
        """
        Осуществляет денежный перевод для оплаты образовательных услуг в университете
        Возвращает тип bool в зависимости от успеха операции
        Пример вызова
        #poly.MoneyTransf(54000)
        """
#Пример иницаилизации
#поли=Polytech(34000, 7804040077)



#Создает объект типа комната. На вход подаются такие аргументы как
#Площадь комнаты, типа float,
#Количество соседей в комнате, типа int,
#Максимальное количество соседей, типа int
class Room:
    def __init__(self, arg1: float, arg2: int, arg3: int):
        self.AreaOfRoom=arg1
        self.CountRoommates=arg2
        self.MaxRoommates=arg3
    def GetArea(self):
        """
        Возвращает площадь комнаты типа float
        Пример вызова
        Area=room.GetArea()
        """
        return self.AreaOfRoom
    def addRoomMate(self, Man: str):
        if self.MaxRoommates>self.CountRoommates:

            """
            Проверяет возможность подселения человека в комнату и по возможности подселяет его и увеличивает  CountRoommates
            возвращает значение типа boolean в зависимости от успеха операции
            Пример вызова
            room.addRoomMate("Denis")
            """
#Пример иницаилизации
#рум_321=Room(16, 3, 4)



__name__="__main__"
if __name__ == "__main__":
    doctest.testfile("example.txt")
