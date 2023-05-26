# Модуль отчетности
class ReportModule:
    def generateReport(self, forecast_data):
        self.forecast_data = forecast_data
        # Генерация простого текстового отчета
        report = f"Прогноз для данных: {self.forecast_data}"
        return report
