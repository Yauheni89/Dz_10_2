from src.financial_operations import filter_transactions_by_description
from src.processing import filter_by_state, sort_dicts_by_date
from src.utils import read_csv_transactions, read_operations, read_xlsx_transactions
from src.widget import get_data, mask_bank_data


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = read_operations("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_csv_transactions("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_xlsx_transactions("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор. Попробуйте снова.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    while True:
        state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
        ).upper()
        if state not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции '{state}' недоступен.")
        else:
            break

    filtered_transactions = filter_by_state(transactions, state)
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        reverse_order = order == "по убыванию"
        filtered_transactions = sort_dicts_by_date(filtered_transactions)
        if reverse_order:
            filtered_transactions.reverse()

    ruble_only = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower()
    if ruble_only == "да":
        filtered_transactions = [
            t
            for t in filtered_transactions
            if (
                t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
                or t.get("currency_code") == "RUB"
            )
        ]

    search_desc = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    ).lower()
    if search_desc == "да":
        search_string = input("Введите строку для поиска в описании транзакций:\nПользователь: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in filtered_transactions:
        date = get_data(transaction["date"])
        description = transaction["description"]
        from_account = mask_bank_data(transaction.get("from", ""))
        to_account = mask_bank_data(transaction.get("to", ""))
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
