import logging
import sys


class Logger:

    @staticmethod
    def init_console_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

        try:
            import colorama
            colorama.init()
        except ImportError:
            pass
