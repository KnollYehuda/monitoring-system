from concurrent.futures import ThreadPoolExecutor
from os.path import basename
from pathlib import Path
from random import randint, sample

import requests
import yaml
from bs4 import BeautifulSoup

from monitoring_system.redis.redis_manager import RedisManager
from monitoring_system.tasks.celery_utils import celery_app

from ..consts import CELERY_DIR_PATH, WEBSITES
from ..db.db_utils import session_maker
from ..db.models import Image
from ..utils import string_generator


@celery_app.task(
    name="store_randoms_in_file",
    max_retries=5,
)
def store_randoms_in_file() -> None:
    """Generate a YAML file in CELERY_DIR_PATH with a random content string."""

    with Path(CELERY_DIR_PATH / f"task_{randint(1000,5000)}.yaml").open("w") as f:
        config = {"content": string_generator(length=55)}
        yaml.dump(config, f, default_flow_style=False)


@celery_app.task(
    name="store_randoms_in_redis",
    max_retries=5,
)
def store_randoms_in_redis() -> None:
    """Generate a random key-value pair and store it in Redis."""

    redis_manager = RedisManager(host="redis")
    redis_manager.set(key=f"task_{string_generator(10)}", value=string_generator(55))


def sample_website(website):
    """Scrape a given website for image URLs and store them in the database.

    :param website: The URL of the website to scrape.
    """

    soup = BeautifulSoup(requests.get(website, timeout=15).content, "html.parser")
    with session_maker() as session:
        for img_attr in sample(soup.findAll("img"), 5):
            image_source: str = img_attr.get("src")
            if image_source and image_source.startswith("http"):
                session.add(Image(name=basename(image_source), source=image_source))
        session.commit()


@celery_app.task(
    name="store_images_urls",
    max_retries=5,
)
def store_images_urls() -> None:
    """Scrape multiple predefined websites for image URLs and store them in the database."""

    for website in WEBSITES:
        with ThreadPoolExecutor() as executor:
            executor.map(sample_website, [website])
