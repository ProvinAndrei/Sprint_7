import allure
import pytest


@allure.feature("Список заказов")
class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_list(self, order_api):
        with allure.step("Запрос списка заказов"):
            response = order_api.get_orders_list()

        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200

        with allure.step("Проверка структуры ответа"):
            response_data = response.json()
            assert "orders" in response_data
            assert isinstance(response_data["orders"], list)
    
    @allure.title("Получение списка заказов с параметрами")
    @pytest.mark.parametrize("params", [
        {"limit": 10},
        {"page": 0},
        {"limit": 5, "page": 1}
    ])
    def test_get_orders_list_with_params(self, order_api, params):
        with allure.step(f"Запрос списка заказов с параметрами: {params}"):
            response = order_api.get_orders_list(params=params)

        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200
            
        with allure.step("Проверка структуры ответа"):
            response_data = response.json()
            assert "orders" in response_data
            assert isinstance(response_data["orders"], list)