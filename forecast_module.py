import numpy as np
import np.random as random
# Модуль прогнозирования
class ForecastingModule:
    def forecast(self, data):
        # Простой прогноз основанный на процентном изменении
        change_percent = random.uniform(-0.1, 0.1) # Случайное изменение от -10% до +10%
        forecast_price = data['price'] * (1 + change_percent)
        print(f"Forecasted price for {data['ticker']}: {forecast_price}")
        return {"ticker": data['ticker'], "forecast_price": forecast_price}