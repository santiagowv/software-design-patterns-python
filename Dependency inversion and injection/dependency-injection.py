# it's a pattern where we split creating the code from using the object by passing it as a parameter.
# dependency injection is a principle that helps to decrease coupling and increase cohesion.
# with the dependency injection pattern, objects lose the responsability of assembling the dependencies. The dependency injector absorbs that responsability.

class DataFile:
    def save_file(self, data):
        print("Data saved in data file.")

class Window:
    def __init__(self, storage: DataFile):
        self.data = ""
        self.storage = storage

    def write_data(self, data: list[int]):
        self.data = data

    def show_window(self):
        print("Data:")
        print(self.data)

    def save_file(self):
        self.storage.save_file(self.data)

storage = DataFile()
w = Window(storage)
w.write_data([1, 2, 3, 4, 5])
w.show_window()

w.save_file()
