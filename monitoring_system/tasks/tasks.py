from pathlib import Path
from random import choice, randint
from string import ascii_lowercase

import yaml

from monitoring_system.tasks.celery_utils import celery_app


@celery_app.task(
    name="files_generator",
    max_retries=5,
)
def files_generator() -> None:
    with Path(f"/tmp/celery/{randint(1000,5000)}.yaml").open("w") as f:
        config = {"message": "".join(choice(ascii_lowercase) for _ in range(55))}
        yaml.dump(config, f, default_flow_style=False)
        # f.write(''.join(choice(ascii_lowercase) for _ in range(55)))
