class Question:
    """
    Класс - абстракция понятия "вопрос".
    """
    _question: str
    _difficulty: int
    _answer: str
    _user_answer: str

    def __init__(self, question: str, difficulty: int, answer: str):
        self._question = question
        self._difficulty = difficulty
        self._answer = answer
        self._user_answer = None


    def get_question(self):
        return self._question

    def get_difficulty(self):
        return f"{str(self._difficulty)}/5"

    def set_user_answer(self, user_answer: str):
        self._user_answer = user_answer

    def build_question(self):
        return f"Вопрос: {self._question}\nСложность: {self.get_difficulty()}"

    def get_points(self):
        return self._difficulty * 10

    def is_correct(self):
        return self._user_answer == self._answer

    def build_negative_feedback(self):
        return f"Ответ неверный. Верный ответ: {self._answer}"

    def build_positive_feedback(self):
        return f"Ответ верный. Получено {self.get_points()} баллов."
