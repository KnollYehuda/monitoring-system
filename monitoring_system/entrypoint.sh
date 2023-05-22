#!/usr/bin/env bash


case $METHOD in

file-generator-worker)
  mkdir -p /tmp/celery
  exec celery \
    --app=monitoring_system.tasks.celery_utils:celery_app \
    worker \
    --loglevel=INFO \
    --hostname=file_generator_worker@%h \
    --autoscale=8,1 \
    --concurrency=8 \
    -Q file_generator_queue
;;

redis-setter)
  exec celery \
    --app=monitoring_system.tasks.celery_utils:celery_app \
    worker \
    --loglevel=INFO \
    --hostname=redis_setter_worker@%h \
    --autoscale=8,1 \
    --concurrency=8 \
    -Q redis_setter_queue
;;

beat)
exec celery \
     -A  monitoring_system.tasks.celery_utils:celery_beat_app \
      beat \
      -l debug \
;;

esac