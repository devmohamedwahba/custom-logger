import logging


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs.txt')
logger = logging.getLogger(__name__)
logger.warning('test')


