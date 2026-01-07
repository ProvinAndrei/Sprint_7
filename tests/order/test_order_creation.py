import pytest
import allure
from data.test_data import TestData
from utils.generators import generate_unique_first_name, generate_phone_number, generate_address


@allure.feature("Создание заказа")
class TestOrderCreation:
    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ])
    def test_create_order_with_colors(self, order_api, colors):
        """Тест создания заказа с указанием цветов"""
        with allure.step("Подготовка данных заказа"):
            order_data = TestData.get_order_data(
                first_name=generate_unique_first_name(),
                phone=generate_phone_number(),
                address=generate_address(),
                color=colors
            )

        with allure.step("Отправка запроса на создание заказа"):
            response = order_api.create_order(order_data)

        with allure.step("Проверка успешного создания"):
            assert response.status_code == 201

        with allure.step("Проверка наличия track номера"):
            response_data = response.json()
            assert "track" in response_data
            assert isinstance(response_data["track"], int)

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self, order_api):
        """Тест создания заказа без поля color в запросе"""
        with allure.step("Подготовка данных без поля color"):
            order_data = TestData.get_order_data(
                first_name=generate_unique_first_name(),
                phone=generate_phone_number(),
                address=generate_address()
            )
            # Убеждаемся, что поля color нет
            if "color" in order_data:
                del order_data["color"]

        with allure.step("Отправка запроса на создание заказа"):
            response = order_api.create_order(order_data)

        with allure.step("Проверка успешного создания"):
            assert response.status_code == 201
            assert "track" in response.json()

    @allure.title("Создание заказа с обязательными полями")
    def test_create_order_required_fields(self, order_api):
        with allure.step("Подготовка данных только с обязательными полями"):
            order_data = TestData.get_order_data(
                first_name=generate_unique_first_name(),
                color=None
            )

        with allure.step("Отправка запроса на создание заказа"):
            response = order_api.create_order(order_data)

        with allure.step("Проверка успешного создания"):
            assert response.status_code == 201
            assert "track" in response.json()
