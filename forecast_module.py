import numpy as np
import np.random as random
# Модуль прогнозирования
class ForecastingModule:
    def forecast(self, stock_data):
        self.stock_data = stock_data
        # Простой прогноз на основе среднего значения
        forecast = sum(self.stock_data) / len(self.stock_data)
        return forecast