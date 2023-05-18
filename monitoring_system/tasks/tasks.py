import yaml
from random import randint, choice
from monitoring_system.tasks.celery_utils import celery_app
from string import ascii_lowercase
from pathlib import Path


@celery_app.task(
    name="files_generator",
    max_retries=5,
)
def files_generator() -> None:
    with Path(f'/tmp/celery/{randint(1000,5000)}.yaml').open('w') as f:
        config = {
            'message': ''.join(choice(ascii_lowercase) for _ in range(55))
        }
        yaml.dump(config, f, default_flow_style=False)
