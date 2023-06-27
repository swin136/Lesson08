class Question:
    """
    Класс - абстракция понятия "вопрос".
    """
    _question: str
    _difficulty: int
    _answer: str
    _user_answer: str

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

    def get_question(self):
        """
        Зарезервированный геттер. Не используется.
        :return:
        """
        return self._question

    def get_difficulty(self):
        """
        формирует текстовое представление сложности задавемого вопроса.
        :return:
        """
        return f"{str(self._difficulty)}/5"

    def set_user_answer(self, user_answer: str):
        """
        Записывает в поля экземпляра класса введенный поьзователем ответ на заданный вопрос.
        :param user_answer:
        :return:
        """
        self._user_answer = user_answer

    def build_question(self):
        """
        Формирует сообщение о задаваемом вопросе пользователю с категорией сложности вопроса.
        :return:
        """
        return f"Вопрос: {self._question}\nСложность: {self.get_difficulty()}"

    def get_points(self):
        """
        Возращает количество баллов, которые может получить пользователь при правильном ответе на вопрос.
        :return: int
        """
        return self._difficulty * 10

    def is_correct(self):
        """
        Возвращает True при вводе пользователем правильного ответа на вопрос, False - при неправильном.
        :return: bool
        """
        return self._user_answer == self._answer

    def build_negative_feedback(self):
        """
        Формирование сообщения полльзователю о его неправильном ответе на вопрос.
        :return: str
        """
        return f"Ответ неверный. Верный ответ: {self._answer}"

    def build_positive_feedback(self):
        """
        Формирование сообщения для ввыода пользователю о его правильном ответе на вопрос.
        :return: str
        """
        return f"Ответ верный. Получено {self.get_points()} баллов."
