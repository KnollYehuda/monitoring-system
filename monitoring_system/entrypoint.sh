#!/usr/bin/env bash


case $METHOD in

worker)
  exec celery \
    --app=monitoring_system.tasks.celery_utils:celery_app \
    worker \
    --loglevel=INFO \
    --hostname=file_generator_worker@%h \
    --autoscale=8,1 \
    --concurrency=8 \
    -Q file_generator_queue
;;

beat)
exec celery \
     -A  monitoring_system.tasks.celery_utils:celery_beat_app \
      beat \
      -l debug \
;;

esac