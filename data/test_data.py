from datetime import datetime, timedelta
from utils.generators import generate_phone_number, generate_address


class TestData:

    @staticmethod
    def get_order_data(
            first_name="Александр",
            last_name="Петров",
            address=None,
            metro_station=4,
            phone=None,
            rent_time=5,
            delivery_date=None,
            comment="Доставка самоката",
            color=None
    ):
        # Генерируем данные, если они не переданы
        if address is None:
            address = generate_address()
        if phone is None:
            phone = generate_phone_number()
        if delivery_date is None:
            delivery_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            
        order_data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }

        if color is not None:
            order_data["color"] = color

        return order_data
    
    @staticmethod
    def get_valid_colors():
        return ["BLACK", "GREY"]
    
    @staticmethod
    def get_metro_stations():
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]