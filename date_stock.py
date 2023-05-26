# импортируем необходимые библиотеки
import requests


# Модуль данных о акциях
class StockDataModule:
    def fetchData(self, ticker):
        # Мы используем фиктивный API для получения данных.
        # В реальной жизни вам следовало бы использовать реальный API
        url = f"https://fakestockapi.com/ticker/{ticker}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Fetched data for {ticker}")
            # Случайное значение для цены акции
            return {"ticker": ticker, "price": random.randint(100, 1000)}
        else:
            print(f"Failed to fetch data for {ticker}")
            return None