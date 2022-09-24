import logging
import inspect


def custom_logger(loglevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(loglevel)

    filehandler = logging.FileHandler("../automation.log", mode='a')
    filehandler.setLevel(loglevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger






