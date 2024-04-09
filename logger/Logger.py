import logging
import sys


class Logger(logging.Logger):
    """
    Класс для логирования. Логи в файле ./logger/logger.log
    """
    _instance: logging.Logger = None

    def __new__(cls, **kwargs):
        if cls._instance is not None:
            return cls._instance
        else:
            cls._instance = object.__new__(cls)
            logging.basicConfig(
                filename='./logger/logger.log',
                filemode='a+',
                level=logging.INFO,
                format='%(process)d - %(asctime)s - %(levelname)s - %(message)s',
                encoding="cp1251"
            )
            cls._instance = logging.getLogger()
            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(logging.INFO)
            cls._instance.addHandler(handler)
            return cls._instance
