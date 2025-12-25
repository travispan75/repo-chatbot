import redis

class RedisClient:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=False,
        )

    def enqueue(self, queue: str, payload: bytes) -> None:
        self.client.lpush(queue, payload)

    def dequeue_blocking(self, queue: str, timeout: int = 0) -> bytes | None:
        result = self.client.brpop(queue, timeout=timeout)
        _, payload = result
        return payload
