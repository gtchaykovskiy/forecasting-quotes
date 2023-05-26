class DatabaseModule:
    def storeData(self, forecast_data):
        self.forecast_data = forecast_data
        # Предполагаем, что у нас есть некая функция для взаимодействия с базой данных
        database.store(self.forecast_data)
