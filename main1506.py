from datetime import datetime

class Time:
    @staticmethod
    def count_time(distance, speed):
        return distance / speed

class Driver:
    @staticmethod
    def calculate_fuel_costs(distance, fuel_consumption, price_per_liter):
        liters_needed = (distance / 100) * fuel_consumption
        return round(liters_needed * price_per_liter, 2)

class Product:
    @staticmethod
    def check_date(today_str, expiry_str):
        today = datetime.strptime(today_str, "%Y-%m-%d")
        expiry = datetime.strptime(expiry_str, "%Y-%m-%d")
        return "Срок годности в порядке." if expiry > today else "Срок годности истёк."

if __name__ == "__main__":
    print(f"Время в пути: {Time.count_time(500, 100)} часов")

    cost = Driver.calculate_fuel_costs(500, 7, 50)
    print(f"Стоимость топлива: {cost} руб.")

    today_date = "2023-11-15"
    expiry_date = "2023-12-31"
    print(Product.check_date(today_date, expiry_date))