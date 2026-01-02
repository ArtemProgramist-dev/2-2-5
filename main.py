class ConsoleCalculator:
    def __init__(self):
        self.result = 0
        self.is_new_calculation = True
        self.history = []

    def display_result(self):
        """Отображает текущий оезультат"""
        print(f"Текуший результат: {self.result}")
     
    def add_to_history(self, operation, value, new_result):
        """Добавляет операцию в историю"""
        self.history.append(f"{self.result} {operation} {value} = {new_result}")

    def run(self):
        print("=" * 40)
        print("КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР")
        print("=" * 40)
        print("Доступные операции: +, -, *, /")
        print("Специальные команды")
        print("  AC - сброс калькулятора")
        print("  H - показать историю операции")
        print("  C - очистить историю")
        print("  Q - выход")
        print("=" * 40)

        self.display_result()

        while True:
            try:
                # Ввод операции
                operation = input("\nВведите операцию (+, -, *, /) или команды: ").strip().upper()

                if operation == 'Q':
                    print("Выход из калькулятораю До свидания!")
                    break
                elif operation == 'AC':
                    self.result = 0
                    self.is_new_calculation = True
                    print("\n" + "=" * 40)
                    print("КАЛЬКУЛЯТОР СБРОЩЕН!")
                    print("=" * 40)
                    self.display_result()
                    continue
                elif operation == 'H':
                    self.show_history()
                    continue
                elif operation == 'C':
                    self.history.clear()
                    print("История очищена!")
                    continue
                elif operation not in ('+', '-', '*', '/'):
                    print("Неизвестная операция! Используйте +, -, *, / или команды AC, H, C, Q")
                    continue

                # Ввод числа
                if self.is_new_calculation:
                    print("Начинаем новое вычисление!")
                    value = input("Введите число: ").strip()
                else:
                    print(f"Текущий результат: {self.result}")
                    value = input("Введите следующее число: ").strip()
                
                # Проверка на команды в поле числа
                if value.upper() == 'AC':
                    self.result = 0
                    self.is_new_calculation = True
                    print("\n" + "=" * 40)
                    print("КАЛЬКУЛЯТОР СБРОШЕН!")
                    print("=" * 40)
                    self.display_result()
                    continue
                elif value.upper() == 'Q':
                    print("Выход из калькулятора. До свидания!")
                    break
                elif value.upper() == 'H':
                    self.show_history()
                    continue
                
                # Преобразование в число
                try:
                    value = float(value)
                except ValueError:
                    print("Ошибка: нужно ввести число!")
                    continue
                
                # Выполнение операции
                old_result = self.result
                
                if operation == '+':
                    self.result += value
                elif operation == '-':
                    self.result -= value
                elif operation == '*':
                    self.result *= value
                elif operation == '/':
                    if value == 0:
                        print("Ошибка: деление на ноль!")
                        continue
                    self.result /= value
                
                # Добавляем в историю и отображаем результат
                self.add_to_history(operation, value, self.result)
                print(f"{old_result} {operation} {value} = {self.result}")
                self.is_new_calculation = False
                
                # Предложение продолжить
                choice = input("\nПродолжить вычисления с этим результатом? (Y/N): ").strip().upper()
                if choice == 'N':
                    self.result = 0
                    self.is_new_calculation = True
                    print("\n" + "=" * 40)
                    print("НАЧИНАЕМ НОВОЕ ВЫЧИСЛЕНИЕ")
                    print("=" * 40)
                    self.display_result()
                
            except KeyboardInterrupt:
                print("\n\nПрограмма прервана пользователем.")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
    
    def show_history(self):
        """Показывает историю операций"""
        if not self.history:
            print("\nИстория пуста")
        else:
            print("\n" + "=" * 40)
            print("ИСТОРИЯ ОПЕРАЦИЙ:")
            print("=" * 40)
            for i, operation in enumerate(self.history, 1):
                print(f"{i}. {operation}")
            print("=" * 40)


# Запуск калькулятора
if __name__ == '__main__':
    ConsoleCalculator().run()

