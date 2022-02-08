# 1. Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from tkinter import Canvas, Tk


class TrafficLight(Tk):
    __color = 'red'

    def __init__(self):
        super().__init__()
        self.title('Светофор')
        self.canvas = Canvas(self, width=200, height=200)
        self.red = self.canvas.create_oval(10, 10, 60, 60, fill=self.__color)
        self.yellow = self.canvas.create_oval(10, 70, 60, 120, fill='black')
        self.green = self.canvas.create_oval(10, 130, 60, 180, fill='black')
        self.canvas.pack()
        self.state = 'red-yellow'
        self.after(7000, self.running)

    def running(self):
        if self.state == 'red-yellow':
            self.canvas.itemconfigure(self.red, fill='black')
            self.canvas.itemconfigure(self.yellow, fill='yellow')
            self.state = 'yellow-green'
            self.after(2000, self.running)
        elif self.state == 'yellow-green':
            self.canvas.itemconfigure(self.yellow, fill='black')
            self.canvas.itemconfigure(self.green, fill='green')
            self.state = 'green-yellow'
            self.after(7000, self.running)
        elif self.state == 'green-yellow':
            self.canvas.itemconfigure(self.green, fill='black')
            self.canvas.itemconfigure(self.yellow, fill='yellow')
            self.state = 'yellow-red'
            self.after(2000, self.running)
        elif self.state == 'yellow-red':
            self.canvas.itemconfigure(self.red, fill=self.__color)
            self.canvas.itemconfigure(self.yellow, fill='black')
            self.state = 'red-yellow'
            self.after(7000, self.running)


a = TrafficLight()
a.mainloop()
