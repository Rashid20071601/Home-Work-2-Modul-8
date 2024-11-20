def personal_sum(numbers):
    # Инициализация переменных: для суммы чисел и подсчёта некорректных данных
    result = 0
    incorrect_data = 0

    # Перебираем элементы в переданном списке
    for element in numbers:
        try:
            # Проверяем, если элемент - строка, выводим предупреждение и увеличиваем счётчик ошибок
            if isinstance(element, str):
                print(f"Некорректный тип данных для подсчёта суммы - {element}")
                incorrect_data += 1
            else:
                # Если элемент корректный, добавляем его к общей сумме
                result += element
        except TypeError:
            # Если возникла ошибка типа, увеличиваем счётчик некорректных данных
            incorrect_data += 1

    # Возвращаем сумму и количество некорректных элементов
    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Вызываем функцию подсчёта суммы и получаем количество некорректных данных
        total_sum, incorrect_data = personal_sum(numbers)
        # Вычисляем количество корректных элементов
        quantity = len(numbers) - incorrect_data

        try:
            # Пытаемся вычислить среднее значение
            result = total_sum / quantity
        except ZeroDivisionError:
            # Если деление на ноль, возвращаем 0
            return 0
    except TypeError:
        # Если входные данные некорректные (например, передано нечто, что нельзя перебирать), выводим сообщение
        print("В numbers записан некорректный тип данных")
        return None

    # Возвращаем результат вычисления среднего значения
    return result


# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
