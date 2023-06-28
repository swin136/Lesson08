import requests
import inspect
import time
import os
import random
from apps.question import Question
from apps.mylogger import MyLoger


# Заголовки для работы requests.get
headers = {
    "Accept": "*/*",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Внешний ресур с вопросами для тестирования
# questions_url = 'https://jsonkeeper.com/b/UF6R'
# Мой основной
# questions_url = 'https://jsonkeeper.com/b/56B1'
# История и география
questions_url = 'https://jsonkeeper.com/b/WDFB'

# Каталог для хранения служебных файлов проекта
APPS_DIR = 'apps'
# Имя файла для хранения логов
log_file = 'data.log'


def get_connection(url: str, site_headers: dict, attempts: int, is_log=True, verify=True):
    """
    Загружает данные с внешнего ресурса. При неудачной попытке загрузки осуществляется повтор.
    :param url: ссылка на ресурс с JSON-данными
    :param site_headers: заголовки из парсеров
    :param attempts: количество повторных попыток для доступа к ресурсу
    :param is_log: включение ведения логирования
    :param verify: включение проверки SSL-сертефиката
    :return: Response object (None в случае ошибок доступа)
    """
    try:
        response = requests.get(url=url, headers=site_headers, verify=verify)
        return response
    except Exception as e:
        if is_log:
            log = MyLoger(os.path.join(APPS_DIR, log_file))
            log.write_log(f"При доступе к ресурсу {url} возникла ошибка: {type(e).__name__} >>> "
                          f"модуль {inspect.stack()[0][1]}: функция {inspect.stack()[0][3]}: "
                          f"строка {inspect.stack()[0][2]}")
        if attempts:
            time.sleep(3)
            get_connection(url=url, site_headers=site_headers, attempts=attempts - 1, is_log=is_log, verify=verify)
        else:
            return


def calculate_user_result(questions: list):
    """
    Считаем статистику пользователя
    :param questions: список экземпляров класса Question
    :return: dict
    """
    # инициализируем счетчики
    total_questions = right_answers = total_score = 0
    for total_questions, question in enumerate(questions, start=1):
        if question.is_ask_question():
            if question.score:
                right_answers += 1
                total_score += question.score

    return {
        'total_questions': total_questions,
        'right_answers': right_answers,
        'total_score': total_score
    }


def load_questions():
    """
    Получает список вопросов с внешнего ресурса. Возвращает список экземпляров класса Question
    :return: list, элементы которого экземпляры класса Question, или None в случае падения программы
    """
    response = get_connection(url=questions_url, site_headers=headers, attempts=3, verify=False)
    if response is not None:
        try:
            user_questions = [Question(item['question'], item['difficulty'], item['answer'])
                              for item in response.json()]
            random.shuffle(user_questions)  # Перемешиваем список
            return user_questions

        except requests.exceptions.JSONDecodeError as error:
            log = MyLoger(os.path.join(APPS_DIR, log_file))
            log.write_log(f"При чтении данных JSON с ресурса {questions_url} возникла ошибка: "  
                          f"{type(error).__name__} >>> модуль {inspect.stack()[0][1]}: "
                          f"функция {inspect.stack()[0][3]}: строка {inspect.stack()[0][2]}")
            return

        except TypeError as terror:
            log = MyLoger(os.path.join(APPS_DIR, log_file))
            log.write_log(f"При преобразовании JSON-данных с ресурса {questions_url} возникла ошибка: "
                          f"{type(terror).__name__} >>> модуль {inspect.stack()[0][1]}: "
                          f"функция {inspect.stack()[0][3]}: строка {inspect.stack()[0][2]}")
            return

    else:
        print(f'Ошибка доступа к ресурсу {questions_url}')
        return
