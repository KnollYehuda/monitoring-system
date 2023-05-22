from celery import Celery


class CeleryConfig:
    """
    Celery configuration object.
    """

    broker_url = "pyamqp://guest:guest@rabbitmq:5672//"
    result_extended = False
    task_always_eager = False
    task_track_started = True
    task_create_missing_queues = True

    result_backend = "redis://redis:6379/0"

    imports = ("monitoring_system.tasks.tasks",)
    broker_transport_options = {
        "max_retries": 10,
        "interval_start": 0,
        "interval_step": 0.2,
        "interval_max": 0.5,
    }
    worker_hijack_root_logger = False
    worker_prefetch_multiplier = 1


def init_celery_app() -> Celery:
    current_celery_app = Celery()
    current_celery_app.config_from_object(CeleryConfig())
    return current_celery_app


# celery worker app
celery_app = init_celery_app()

# celery beat app
celery_beat_app = init_celery_app()
celery_beat_app.conf.update(
    {
        "CELERYBEAT_SCHEDULE": {
            "files_generator": {
                "task": "files_generator",
                "options": {"queue": "file_generator_queue"},
                "schedule": 15.0,
            },
            "redis_setter": {
                "task": "redis_setter",
                "options": {"queue": "redis_setter_queue"},
                "schedule": 5.0,
            },
        }
    }
)
