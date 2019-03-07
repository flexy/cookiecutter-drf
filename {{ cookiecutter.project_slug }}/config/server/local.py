from .base import BaseUvicornWorker


class LocalUvicornWorker(BaseUvicornWorker):
    def __init__(self, *args, **kwargs):
        self.CONFIG_KWARGS['debug'] = True
        return super().__init__(*args, **kwargs)
