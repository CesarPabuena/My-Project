import os
from utils.constants import Settings


class Connection:

    URL = f'postgresql+psycopg2://{Settings.DB_USER}:{Settings.DB_PASSWORD}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}'
    ACTIVE_MODIFICATE = True