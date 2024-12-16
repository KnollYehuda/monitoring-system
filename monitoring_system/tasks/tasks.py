from os.path import basename
from pathlib import Path
from random import randint, sample

import requests
import yaml
from bs4 import BeautifulSoup

from monitoring_system.redis.redis_manager import RedisManager
from monitoring_system.tasks.celery_utils import celery_app

from ..consts import CELERY_DIR_PATH
from ..db.db_utils import session_maker
from ..db.models import Image
from ..utils import string_generator


@celery_app.task(
    name="files_generator",
    max_retries=5,
)
def files_generator() -> None:
    """Generate a new yaml file in CELERY_DIR_PATH"""

    with Path(CELERY_DIR_PATH / f"task_{randint(1000,5000)}.yaml").open("w") as f:
        config = {"content": string_generator(length=55)}
        yaml.dump(config, f, default_flow_style=False)


@celery_app.task(
    name="redis_setter",
    max_retries=5,
)
def redis_setter() -> None:
    """Generate a key-value and insert it to redis"""

    redis_manager = RedisManager(host="redis")
    redis_manager.set(key=f"task_{string_generator(10)}", value=string_generator(55))


@celery_app.task(
    name="backup_tasks_to_db",
    max_retries=5,
)
def backup_tasks_to_db() -> None:
    soup = BeautifulSoup(requests.get("https://ynet.co.il").content, "html.parser")
    with session_maker() as session:
        for img_attr in sample(soup.findAll("img"), 5):
            image_source = img_attr.get("src")
            if image_source:
                session.add(Image(name=basename(image_source), source=image_source))
        session.commit()
