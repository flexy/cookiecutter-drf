import os

from .base import BaseUvicornWorker


class TestUvicornWorker(BaseUvicornWorker):
    def __init__(self, *args, **kwargs):
        # Travis uses 2 workers
        _is_travis = os.environ.get("TRAVIS") == "true"
        if _is_travis:
            self.CONFIG_KWARGS["workers"] = 2

        return super().__init__(*args, **kwargs)
