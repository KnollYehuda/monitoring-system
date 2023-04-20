import datetime
import yaml
from random import randint
from datetime import datetime
from monitoring_system.tasks.celery_utils import celery_app


@celery_app.task(
    name="files_generator",
    max_retries=5,
)
def files_generator() -> None:
    with open(f'/tmp/celery/{randint(1000,5000)}', "wb") as target_file:
        yaml.safe_dump({
            'now': datetime.now()
        }, target_file, default_flow_style=True)
