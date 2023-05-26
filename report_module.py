# Модуль отчетности
class ReportModule:
    def generateReport(self, forecast_data):
        print(f"Report:\nTicker: {forecast_data['ticker']}\nForecast Price: {forecast_data['forecast_price']}")