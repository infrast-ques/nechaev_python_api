import json
import logging
import sys

from colorama import Style, Fore

from src.module.api.requests.implementation.TRequest import TRequest


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

    @staticmethod
    def request_log(logger, url: str, request: TRequest):
        logger.info(f'\n{Fore.RED}Request START: ─────────────────────────────────────── {Style.RESET_ALL}')
        logger.info(f'Sending url: {Style.BRIGHT}{request.method.value} - {url}{Style.RESET_ALL}')
        if request.headers is not None:
            logger.info(f'Sending headers:\n{Style.BRIGHT}{request.headers}{Style.RESET_ALL}')
        else:
            logger.info(f'Sending headers:')
        if request.cookies is not None:
            logger.info(f'Sending cookies:\n{Style.BRIGHT}{request.cookies}{Style.RESET_ALL}')
        else:
            logger.info(f'Sending cookies:')
        if request.body is not None:
            logger.info(f'Sending body:\n{Style.BRIGHT}{json.dumps(request.body, indent=4)}{Style.RESET_ALL}')
        else:
            logger.info(f'Sending body:')
        logger.info(f'{Fore.RED}Request END: ─────────────────────────────────────── {Style.RESET_ALL}')

    @staticmethod
    def response_log(logger, response):
        logger.info(f'{Fore.RED}Response START: ─────────────────────────────────────── {Style.RESET_ALL}')
        logger.info(f'Response code {Style.BRIGHT}{response.status_code}{Style.RESET_ALL}')
        logger.info(f'Response body:\n{Style.BRIGHT}{json.dumps(json.loads(response.text), indent=4)}{Style.RESET_ALL}')
        logger.info(f'{Fore.RED}Response END: ─────────────────────────────────────── {Style.RESET_ALL}')
        logger.info('\n')
