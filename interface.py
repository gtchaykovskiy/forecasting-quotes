import * from date_stock
import * from forecast_module
import * from report_module

# Интерфейс пользователя
class UserInterface:
    def displayData(self, stock_data):
        self.stock_data = stock_data
        # Простой вывод данных об акциях
        print(self.stock_data)


# Подключаем модули и выполняем основной код
stock_data_module = StockDataModule()
forecast_module = ForecastingModule()
report_module = ReportModule()
user_interface = UserInterface()

ticker = user_interface.getInput()
data = stock_data_module.fetchData(ticker)
if data is not None:
    forecast_data = forecast_module.forecast(data)
    report_module.generateReport(forecast_data)