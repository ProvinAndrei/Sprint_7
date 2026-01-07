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
