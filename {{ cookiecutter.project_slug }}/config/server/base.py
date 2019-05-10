from uvicorn.workers import UvicornWorker
import multiprocessing


class BaseUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {"lifespan": "off", "workers": multiprocessing.cpu_count()}
