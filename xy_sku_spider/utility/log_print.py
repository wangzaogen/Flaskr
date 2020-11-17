import time
from loguru import logger
from pathlib import Path





class Loggings(object):

    def __init__(self,site):
        project_path = Path.cwd().parent
        log_path = Path(project_path, "log/{}".format(site))
        t = time.strftime("%Y_%m_%d")
        print(str(log_path))
        self.logger = logger
        self.logger.add(f"{log_path}/{site}_log_{t}.log", rotation="500MB", encoding="utf-8", enqueue=True,
                   retention="10 days")
        self.logger.info("init.......")


    def info(self, msg):
        return self.logger.info(msg)

    def debug(self, msg):
        return self.logger.debug(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)

if __name__ == '__main__':
    loggings = Loggings('test')
    loggings.info("中文test")
    loggings.debug("中文test")
    loggings.warning("中文test")
    loggings.error("中文test")

    logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
    n1 = "cool"
    n2 = [1, 2, 3]
    logger.info(f'If you are using Python {n1}, prefer {n2} of course!')