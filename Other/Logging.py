import logging


def directories(function):
    count = 0
    for key in dir(function):
        if not key.__contains__("_"):
            count +=1
            print(key, end=", ")
        if count % 15 == 0:
            print()


# directories(logging)  # Prints dir(logging) w/o _s
# print(logger.level)  # Prints logger level, 0 NOTSET, 10 DEBUG, 20 INFO, 30 WARNING, 40 ERROR, 50 CRITICAL

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log1.txt",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w")  # "a" to append, "w" to write

logger = logging.getLogger()
logger.info("First message")

logger.debug("300")
logger.warning("400000")