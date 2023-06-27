from datetime import datetime


class MyLoger:
    """
    Класс для сохранения логов работы программы.
    """
    __is_print: bool
    __file_log: str

    def __init__(self, file_log: str, is_print=True):
        self.__is_print = is_print
        self.__file_log = file_log
        self.type_msg = ("Error", "Info", "Debug")

    def write_log(self, log_msg: str, index_msg=0):
        """
        Пишет лог ошибки(сообщения в файл). Может также выводить текст на консоль.
        :param log_msg:
        :param index_msg:
        :return: None
        """
        # При необходимости вывожу сообщение на консоль
        if self.__is_print:
            print(log_msg)
        try:
            with open(file=self.__file_log, mode="at", encoding="utf-8") as file:
                date = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
                file.write(f"{self.type_msg[index_msg]}: {date} : {log_msg}\n")
        except:
            print("При записи лога возникла ошибка!")
