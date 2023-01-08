import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class DatabaseConnection:
    def connect(self) -> pd.DataFrame:
        print("Connection succesful...")
        data = sns.load_dataset("tips")
        return data

    def get_data(self) -> pd.DataFrame:
        data = self.connect()
        return data

class DataProcessing:
    def process_data(self, data: pd.DataFrame) -> pd.DataFrame:
        data = data[["day", "time", "total_bill"]].groupby(["day", "time"]).sum().reset_index()
        days_number = {"Thur":1, "Fri":2, "Sat":3, "Sun":4}
        data["day"] = data["day"].apply(lambda x:days_number.get(x))
        return data

class DataVisualization:
    def generate_visual(self, data: pd.DataFrame):
        sns.set()
        sns.lineplot(data = data, x = "day", y ="total_bill", hue = "time")
        plt.show()

class SalesReport:
    def __init__(self) -> None:
        self.data = DatabaseConnection()
        self.processingtool = DataProcessing()
        self.visualizationtool = DataVisualization()

    def generate_report(self):
        data = self.data.get_data()
        data = self.processingtool.process_data(data)
        self.visualizationtool.generate_visual(data)

if __name__ == "__main__":
    report = SalesReport()
    report.generate_report()