import logging
import pytz
from datetime import datetime

class Logger:

    def __init__(self,_logname) -> None:
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(f'log-{_logname}')
    
    def info(self, _msg):
        """ Print info level log message"""
        _msg = f"{_msg}"
        print(_msg)
        return self.logger.info(_msg)
