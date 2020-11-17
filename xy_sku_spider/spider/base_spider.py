

import threading
from xy_sku_spider.utility.date import *
import random

thread_pool_size = 50

RANDOM_DELAY = False


class BaseSpider(object):
    @staticmethod
    def random_delay():
        if RANDOM_DELAY:
            time.sleep(random.randint(0, 16))

    def __init__(self, name):
        self.name = name
        print('Today date is: %s' % self.date_string)

        print("Target site is {0}.cn".format(name))
        self.mutex = threading.Lock()  # 创建锁



