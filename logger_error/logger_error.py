import logging

logger = logging.getLogger('stopcard')
formatter = logging.Formatter('%(created)s-%(asctime)s-%(levelname)s-%(message)s')
filehandler = logging.FileHandler('stopcard.txt')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.setLevel(logging.INFO)

def loggerError(*args):
    logger.error(args)
