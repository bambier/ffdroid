import logging

logger = logging.getLogger("application")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)


formatter = logging.Formatter(
    '%(levelname)s - %(filename)s:%(lineno)d - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
