from redis import Redis


class RedisManager:
    """The redis service manager
    :param host: dynamic host, default value is localhost"""

    def __init__(self, host: str = "127.0.0.1"):
        self.redis_cli = Redis(host=host, decode_responses=True)

    def set(self, key: str, value: str):
        """Insert a new key-value to redis"""

        self.redis_cli.set(key, value)

    def get(self, key):
        """Get value from redis by given key"""

        return self.redis_cli.get(key)
