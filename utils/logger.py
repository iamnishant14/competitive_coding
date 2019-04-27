"""
Author: Nishant

Problem : Custom logger for the project.

Date : 10/05/2019
"""
import logging
from logging.handlers import RotatingFileHandler


class CompetitiveCodingLogger:

    def __init__(self, logger_name='debug.log', logging_mode='Debug', max_bytes=10000, backup_count=2,
                 module_name='utils'):
        self.__logger_name = logger_name
        self.__max_bytes = max_bytes
        self.__logging_mode = logging_mode
        self.__backup_count = backup_count
        self.__module_name = module_name

    def __get_handler(self):
        handler = RotatingFileHandler(self.__logger_name, self.__logging_mode, self.__max_bytes, self.__backup_count)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        return handler

    def get_logger(self):
        logger = logging.getLogger(self.__module_name)
        logger.setLevel(logging.INFO)
        handler = self.__get_handler()
        logger.addHandler(handler)
        return logger
