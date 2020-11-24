import redis

class RedisSubscriber(object):
    """
    Redis频道订阅辅助类
    """

    def __init__(self, channel):
        # 连接redis
        self.db = redis.StrictRedis(host='127.0.0.1', port=6379, password=None, db=0, decode_responses=True)
        self.channel = channel  # 定义频道名称

    def psubscribe(self):
        """
        订阅方法
        """
        pub = self.db.pubsub()
        pub.psubscribe(self.channel)  # 同时订阅多个频道，要用psubscribe
        pub.listen()
        return pub

    def psubscribe_key(self):
        """
        订阅键过期事件
        :return:
        """
        pub = self.db.pubsub()
        pub.psubscribe("__keyevent@0__:expired") # 订阅所有过期事件
        # pub.psubscribe("__keyspace@0__:title") # 订阅key=title 的所有事件
        pub.listen()
        return pub

if __name__ == '__main__':

    subscriber = RedisSubscriber(['wang'])
    redis_sub = subscriber.psubscribe_key()
    # redis_sub = subscriber.psubscribe()   # 调用订阅方法
    #
    # while True:
    #     msg = redis_sub.parse_response(block=False, timeout=60)
    #     print("收到订阅消息 %s" % msg)

    while True:
        msg = redis_sub.parse_response(block=False, timeout=60)
        print("收到订阅消息 %s" % msg)


