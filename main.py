# Tema S30 Python
# 1. Implementati o clasa Termometru cu metodele “cald” si “rece”. Aceasta clasa contine o
# proprietate “temperatura” care creste sau scade la fiecare apelare a uneia din metode.
# Implementati aceasta clasa folosind Observer pattern astfel incat sa puteti observa temperatura
# si sa o afisati in consola.


class Observer:
    def update(self, temperatura):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, temperatura):
        for observer in self._observers:
            observer.update(temperatura)

class Termometru(Subject):
    def __init__(self):
        super().__init__()
        self._temperatura = 0

    def set_temperatura(self, temperatura):
        self._temperatura = temperatura
        self.notify(temperatura)

    def cald(self):
        self._temperatura += 1
        self.notify(self._temperatura)

    def rece(self):
        self._temperatura -= 1
        self.notify(self._temperatura)


class ConsoleObserver(Observer):
    def update(self, temperatura):
        print(f"Temperatura curentă este: {temperatura}°C")

if __name__ == "__main__":
    termometru = Termometru()

    
    console_observer = ConsoleObserver()
    termometru.attach(console_observer)

    termometru.cald()
    termometru.rece()
    termometru.cald()
