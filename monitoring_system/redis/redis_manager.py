from redis import Redis


class RedisManager:
    def __init__(self, host: str = "127.0.0.1"):
        self.redis_cli = Redis(host=host, decode_responses=True)

    def set(self, key: str, value: str):
        self.redis_cli.set(key, value)

    def get(self, key):
        return self.redis_cli.get(key)
