from threading import Lock

lock = Lock()


class Singleton(type):
    """
    Thread Safe Singleton
     See at https://stackoverflow.com/questions/50566934/why-is-this-singleton-implementation-not-thread-safe
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(
                        *args, **kwargs
                    )
        return cls._instances[cls]

    @classmethod
    def clear_instances(cls):
        cls._instances = {}