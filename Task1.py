# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Smartphone:
    """Класс, описывающий смартфон"""

    def __init__(self, brand: str, model: str, battery_level: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Производитель смартфона
        :param model: Модель смартфона
        :param battery_level: Уровень заряда батареи (в процентах)

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 85)
        >>> phone.brand
        'Apple'
        >>> phone.model
        'iPhone 14'
        >>> phone.battery_level
        85
        """
        if not isinstance(brand, str):
            raise TypeError("Производитель должен быть строкой")
        if not brand.strip():
            raise ValueError("Производитель не может быть пустой строкой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not model.strip():
            raise ValueError("Модель не может быть пустой строкой")
        self.model = model

        if not isinstance(battery_level, (int, float)):
            raise TypeError("Уровень заряда должен быть числом")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("Уровень заряда должен быть от 0 до 100")
        self.battery_level = battery_level

    def make_call(self, phone_number: str, duration: int) -> bool:
        """
        Совершение телефонного звонка

        :param phone_number: Номер телефона для звонка
        :param duration: Длительность звонка в секундах
        :return: Успешность совершения звонка
        :raise ValueError: Если номер телефона некорректный или длительность отрицательная

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 90)
        >>> phone.make_call("+79123456789", 60)
        True
        """
        if not isinstance(phone_number, str):
            raise TypeError("Номер телефона должен быть строкой")
        if not phone_number.strip():
            raise ValueError("Номер телефона не может быть пустым")
        if not isinstance(duration, int):
            raise TypeError("Длительность звонка должна быть целым числом")
        if duration <= 0:
            raise ValueError("Длительность звонка должна быть положительным числом")

        # Имитация успешного звонка
        return True

    def install_app(self, app_name: str, required_storage: Union[int, float]) -> bool:
        """
        Установка приложения на смартфон

        :param app_name: Название приложения
        :param required_storage: Требуемый объем памяти (в МБ)
        :return: Успешность установки
        :raise ValueError: Если название приложения пустое или требуемый объем памяти некорректен

        Примеры:
        >>> phone = Smartphone("Google", "Pixel 7", 50)
        >>> phone.install_app("Telegram", 250)
        True
        """
        if not isinstance(app_name, str):
            raise TypeError("Название приложения должно быть строкой")
        if not app_name.strip():
            raise ValueError("Название приложения не может быть пустым")
        if not isinstance(required_storage, (int, float)):
            raise TypeError("Требуемый объем памяти должен быть числом")
        if required_storage <= 0:
            raise ValueError("Требуемый объем памяти должен быть положительным числом")

        # Имитация успешной установки
        return True

    def charge(self, charge_amount: Union[int, float]) -> int:
        """
        Зарядка смартфона

        :param charge_amount: Количество заряда для добавления (в процентах)
        :return: Текущий уровень заряда после зарядки
        :raise ValueError: Если количество заряда отрицательное или превышает 100

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Mi 13", 20)
        >>> phone.charge(30)
        50
        """
        if not isinstance(charge_amount, (int, float)):
            raise TypeError("Количество заряда должно быть числом")
        if charge_amount < 0:
            raise ValueError("Количество заряда должно быть положительным числом")

        # Имитация зарядки
        self.battery_level = min(100, self.battery_level + charge_amount)
        return self.battery_level


class EBook:
    """Класс, описывающий электронную книгу"""

    def __init__(self, title: str, author: str, current_page: int, total_pages: int):
        """
        Создание и подготовка к работе объекта "Электронная книга"

        :param title: Название книги
        :param author: Автор книги
        :param current_page: Текущая страница
        :param total_pages: Общее количество страниц

        Примеры:
        >>> book = EBook("Война и мир", "Лев Толстой", 1, 1300)
        >>> book.title
        'Война и мир'
        >>> book.current_page
        1
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(current_page, int):
            raise TypeError("Номер текущей страницы должен быть целым числом")
        if current_page <= 0:
            raise ValueError("Номер текущей страницы должен быть положительным числом")
        self.current_page = current_page

        if not isinstance(total_pages, int):
            raise TypeError("Общее количество страниц должно быть целым числом")
        if total_pages <= 0:
            raise ValueError("Общее количество страниц должно быть положительным числом")
        if current_page > total_pages:
            raise ValueError("Текущая страница не может быть больше общего количества страниц")
        self.total_pages = total_pages

    def go_to_page(self, page_number: int) -> int:
        """
        Переход на указанную страницу

        :param page_number: Номер страницы для перехода
        :return: Номер текущей страницы после перехода
        :raise ValueError: Если номер страницы вне допустимого диапазона

        Примеры:
        >>> book = EBook("Преступление и наказание", "Федор Достоевский", 1, 500)
        >>> book.go_to_page(100)
        100
        """
        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть целым числом")
        if page_number <= 0 or page_number > self.total_pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.total_pages}")

        self.current_page = page_number
        return self.current_page

    def get_reading_progress(self) -> float:
        """
        Получение прогресса чтения в процентах

        :return: Процент прочитанных страниц

        Примеры:
        >>> book = EBook("1984", "Джордж Оруэлл", 100, 328)
        >>> round(book.get_reading_progress(), 1)
        30.5
        """
        progress = (self.current_page / self.total_pages) * 100
        return round(progress, 1)

    def bookmark_page(self) -> int:
        """
        Добавление текущей страницы в закладки

        :return: Номер страницы, добавленной в закладки

        Примеры:
        >>> book = EBook("Мастер и Маргарита", "Михаил Булгаков", 250, 480)
        >>> book.bookmark_page()
        250
        """
        # Имитация добавления закладки
        return self.current_page


class OnlineStore:
    """Класс, описывающий интернет-магазин"""

    def __init__(self, name: str, website: str, rating: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Интернет-магазин"

        :param name: Название магазина
        :param website: Адрес веб-сайта
        :param rating: Рейтинг магазина (от 0 до 5)

        Примеры:
        >>> store = OnlineStore("Ozon", "https://www.ozon.ru", 4.5)
        >>> store.name
        'Ozon'
        >>> store.rating
        4.5
        """
        if not isinstance(name, str):
            raise TypeError("Название магазина должно быть строкой")
        if not name.strip():
            raise ValueError("Название магазина не может быть пустым")
        self.name = name

        if not isinstance(website, str):
            raise TypeError("Адрес сайта должен быть строкой")
        if not website.strip():
            raise ValueError("Адрес сайта не может быть пустым")
        self.website = website

        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен быть числом")
        if rating < 0 or rating > 5:
            raise ValueError("Рейтинг должен быть от 0 до 5")
        self.rating = rating

        self.cart = []  # Корзина покупателя

    def add_to_cart(self, product_id: str, quantity: int) -> dict:
        """
        Добавление товара в корзину

        :param product_id: Идентификатор товара
        :param quantity: Количество товара
        :return: Информация о добавленном товаре
        :raise ValueError: Если идентификатор пустой или количество некорректно

        Примеры:
        >>> store = OnlineStore("Wildberries", "https://www.wildberries.ru", 4.2)
        >>> store.add_to_cart("12345", 2)
        {'product_id': '12345', 'quantity': 2}
        """
        if not isinstance(product_id, str):
            raise TypeError("Идентификатор товара должен быть строкой")
        if not product_id.strip():
            raise ValueError("Идентификатор товара не может быть пустым")
        if not isinstance(quantity, int):
            raise TypeError("Количество товара должно быть целым числом")
        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным числом")

        item = {"product_id": product_id, "quantity": quantity}
        self.cart.append(item)
        return item

    def make_order(self, address: str, payment_method: str) -> float:
        """
        Оформление заказа

        :param address: Адрес доставки
        :param payment_method: Способ оплаты
        :return: Общая сумма заказа
        :raise ValueError: Если адрес или способ оплаты пустые

        Примеры:
        >>> store = OnlineStore("Яндекс Маркет", "https://market.yandex.ru", 4.3)
        >>> store.make_order("ул. Ленина, д. 1", "Банковская карта")
        0.0
        """
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой")
        if not address.strip():
            raise ValueError("Адрес не может быть пустым")
        if not isinstance(payment_method, str):
            raise TypeError("Способ оплаты должен быть строкой")
        if not payment_method.strip():
            raise ValueError("Способ оплаты не может быть пустым")

        # Имитация оформления заказа
        total = sum(len(item["product_id"]) * item["quantity"] for item in self.cart) * 0.1
        self.cart.clear()
        return round(total, 2)

    def leave_review(self, user_name: str, review_text: str, rating: Union[int, float]) -> dict:
        """
        Оставление отзыва о магазине

        :param user_name: Имя пользователя
        :param review_text: Текст отзыва
        :param rating: Оценка магазина
        :return: Информация об оставленном отзыве
        :raise ValueError: Если данные некорректны

        Примеры:
        >>> store = OnlineStore("AliExpress", "https://aliexpress.ru", 4.0)
        >>> store.leave_review("Иван Иванов", "Отличный магазин!", 5)
        {'user': 'Иван Иванов', 'rating': 5, 'text': 'Отличный магазин!'}
        """
        if not isinstance(user_name, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not user_name.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        if not isinstance(review_text, str):
            raise TypeError("Текст отзыва должен быть строкой")
        if not review_text.strip():
            raise ValueError("Текст отзыва не может быть пустым")
        if not isinstance(rating, (int, float)):
            raise TypeError("Оценка должна быть числом")
        if rating < 0 or rating > 5:
            raise ValueError("Оценка должна быть от 0 до 5")

        review = {
            "user": user_name,
            "rating": rating,
            "text": review_text
        }
        return review

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
