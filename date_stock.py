# импортируем необходимые библиотеки
import requests


# Модуль данных о акциях
class StockDataModule:
    def updateData(self, stock_name):
        self.stock_name = stock_name
        date.time.add(self)
        # Обновление данных об акциях с использованием API
        new_data = requests.get(f"https://api.stockdata.com/{self.stock_name}")
        return new_data.json()