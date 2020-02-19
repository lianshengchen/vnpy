import logging

class MyLogger:
    """"""
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level = logging.DEBUG)
        handler = logging.FileHandler("log.txt")
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        self.logger.addHandler(console)


    
    def info(self, msg):
        self.logger.info(msg)



    def debug(self, msg):
        self.logger.debug(msg)


    def warning(self, msg):
        self.logger.warning(msg)


    def error(self, msg):
        self.logger.error(msg)





