class Question:
    """
    Класс - абстракция понятия "вопрос".
    """
    _question: str
    _difficulty: int
    _answer: str
    _user_answer: str
    _is_ask: bool
    _score: int

    def __init__(self, question: str, difficulty: int, answer: str):
        """
        Инициализируем поля экземплра класса
        :param question: Вопрос, задаваемый пользователю.
        :param difficulty: Сложность вопроса.
        :param answer: Ответ (правильный) на задаваемый вопрос.
        """
        self._question = question
        self._difficulty = difficulty
        self._answer = answer
        # Поле для хранения ответа пользователя, при инициализации экземплря класса - пустое
        self._user_answer = None
        # Пользователю вопрос не задавался
        self._is_ask = False
        self._score = 0

    def get_difficulty(self):
        """
        формирует текстовое представление сложности задавемого вопроса.
        :return:
        """
        return f"{str(self._difficulty)}/5"

    def set_user_answer(self, user_answer: str):
        """
        Записывает в поля экземпляра класса введенный пользователем ответ на заданный вопрос.
        :param user_answer:
        :return: None
        """
        self._user_answer = user_answer
        # Начисляем баллы пользователю в случае правильного ответа
        if self.is_correct():
            self._score = self.get_points()

    def build_question(self):
        """
        Формирует сообщение о задаваемом вопросе пользователю с категорией сложности вопроса.
        :return:
        """
        # Взводим флаг поля: "задавался ли вопрос пользователю"
        self._is_ask = True
        return f"Вопрос: {self._question}\nСложность: {self.get_difficulty()}"

    def get_points(self):
        """
        Возращает количество баллов, которые может получить пользователь при правильном ответе на вопрос.
        :return: int
        """
        return self._difficulty * 10

    def is_correct(self):
        """
        Возвращает True при совпадении введенного пользователем ответа на вопрос с правильным.
        :return: bool
        """
        return self._user_answer == self._answer

    def build_negative_feedback(self):
        """
        Формирование сообщения пользователю о его неправильном ответе на вопрос.
        :return: str
        """
        return f"Ответ неверный. Верный ответ: {self._answer}"

    def build_positive_feedback(self):
        """
        Формирование сообщения для вывода пользователю о его правильном ответе на вопрос.
        :return: str
        """
        return f"Ответ верный. Получено {self.get_score()} баллов."

    def get_score(self):
        """
        Возращает количесво полученных пользователем баллов за ответ на вопрос.
        :return: int
        """
        return self._score

    def is_ask_question(self):
        """
        Возращает True если пользователю задавался вопрос.
        :return: bool
        """
        return self._is_ask
