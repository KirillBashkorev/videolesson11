import logging
import colorlog
logging.basicConfig(level=logging.DEBUG)

# Настройка цветного логирования
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s'
))

logger = colorlog.getLogger('example')
logger.addHandler(handler)

logger.debug("Подробная информация для отладки")      # DEBUG
logger.info("Общая информация о работе")
logger.warning("Предупреждение о проблеме")   
logger.error("Ошибка в программе")                    # ERROR
logger.critical("Критическая ошибка!")