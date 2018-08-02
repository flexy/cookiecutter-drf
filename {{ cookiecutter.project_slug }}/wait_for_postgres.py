import os
import logging
from time import time, sleep
import psycopg2
check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 30)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"
config = {
    "dbname": os.getenv("POSTGRES_DB", "postgres"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
    "host": os.getenv("DATABASE_URL", "postgres")
}

start_time = time()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def pg_isready(host, user, password, dbname):
    while time() - start_time < check_timeout:
        try:
            conn = psycopg2.connect(**vars())
            logger.info("Postgres is ready! ✨ 💅")
            conn.close()
            return True
        except psycopg2.OperationalError:
            logger.info(
                "Postgres isn't ready. Waiting for {} {}...".format(
                    check_interval,
                    interval_unit,
                )
            )
            sleep(check_interval)

    logger.error(
        "We could not connect to Postgres within {} seconds.".format(
            check_timeout,
        )
    )
    return False


pg_isready(**config)
