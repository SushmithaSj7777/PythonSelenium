import inspect
import logging


def test_logging():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    filehandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel("DEBUG")

    logger.debug("DEBUG messange")
    logger.info("INFO message")
    logger.warning("WARNING message")
    logger.error("ERROR messgae")
    logger.critical("CRITICAL message")
