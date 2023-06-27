from apps.utils import *


def main():
    """
    Основная бизнес-логика приложения
    :return: None
    """
    # Формируем список вопросов для тестирования пользователяЛондон
    questions = load_questions()
    if questions is None:
        print('Критическая ошибка! Работа программы будет завершена.')
        return
    # Цикл опроса пользователя
    print('Игра начинается!')
    for i, question in enumerate(questions, start=1):
        print(question.build_question())
        while True:
            # Считываем ответ пользователя на вопрос
            user_answer = input(f"Введите Ваш вариант ответа на вопрос №{i}: ").strip()
            if user_answer:
                # Записываем ответ пользователя
                question.set_user_answer(user_answer)
                break
        # Вывод результата проверки введенного пользователем ответа
        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    # Считаем статистику всей игры
    result = calculate_user_result(questions)
    # Выводим статистику
    print('Вот и всё!')
    print(f"Всего задано вопросов: {result['total_questions']}")
    print(f"Получено правильных ответов: {result['right_answers']}")
    print(f"Набрано баллов: {result['total_score']}")
    input("[+] Нажмите Enter для завершения работы программы ... ")


if __name__ == "__main__":
    main()
