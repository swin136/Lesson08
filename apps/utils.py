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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Внешний ресур с вопросами для тестирования
# questions_url = 'https://jsonkeeper.com/b/UF6R'
# Мой основной
# questions_url = 'https://jsonkeeper.com/b/56B1'
# История и география
questions_url = 'https://jsonkeeper.com/b/WDFB'

APPS_DIR = 'apps'
log_file = 'data.log'



def get_connection(url: str, site_headers: dict, attempts: int, is_log=True, verify=True):
    """
    Загружает данные с внешнего ресурса. При неудачной попытке загрузки осуществляется повтор.
    :param url:
    :param site_headers:
    :param attempts: количество попыток для доступа к ресурсу
    :param is_log: включение ведения логирования
    :param verify: включение проверки SSL-сертефиката
    :return:
    """
    try:
        response = requests.get(url=url, headers=site_headers, verify=verify)
        return response
    except Exception as e:
        if is_log:
            log = MyLoger(os.path.join(APPS_DIR, log_file))
            log.write_log(f"При доступе к ресурсу {url} возникла ошибка: {type(e).__name__} >>> {inspect.stack()[0]}")
        if attempts:
            time.sleep(3)
            get_connection(url=url, site_headers=site_headers, attempts=attempts - 1, is_log=is_log, verify=verify)
        else:
            return

def calculate_user_result(questions: list):
    """
    Считаем статистику пользователя
    :param questions:
    :return:
    """
    total_questions = right_answers = total_score = 0
    for question in questions:
        total_questions += 1
        if question.is_correct():
            right_answers += 1
            total_score += question.get_points()

    return {
        'total_questions': total_questions,
        'right_answers': right_answers,
        'total_score': total_score
    }

def load_questions():
    """
    Получает список вопросов с внешнего ресурса. Возвращает список экземпляров класса Question
    :return:
    """
    response = get_connection(url=questions_url, site_headers=headers, attempts=3, verify=False)
    if response is not None:
        try:
            user_questions = [Question(item['question'], item['difficulty'], item['answer']) for item in response.json()]
            random.shuffle(user_questions)
            return user_questions
        except requests.exceptions.JSONDecodeError as Error:
            log = MyLoger(os.path.join(APPS_DIR, log_file))
            log.write_log(f"При чтении данных JSON с ресурса {questions_url} возникла ошибка: "  
                          f"{type(Error).__name__} >>> {inspect.stack()[0]}")
            return
    else:
        print(f'Ошибка доступа к ресурсу {questions_url}')
        return

