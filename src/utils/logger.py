import logging

# Codes

DEBUG = True

logger = logging.getLogger("application")
logger.setLevel(logging.DEBUG if DEBUG else logging.CRITICAL)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG if DEBUG else logging.CRITICAL)


formatter = logging.Formatter(
    '%(levelname)s - %(filename)s:%(lineno)d - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
