#!/usr/bin/env bash


case $METHOD in

store-randoms-in-file)
  exec celery \
    --app=monitoring_system.tasks.celery_utils:celery_app \
    worker \
    --loglevel=INFO \
    --hostname=store_randoms_in_file_worker@%h \
    --autoscale=8,1 \
    --concurrency=8 \
    -Q store_randoms_in_file_queue
;;

store-randoms-in-redis)
  exec celery \
    --app=monitoring_system.tasks.celery_utils:celery_app \
    worker \
    --loglevel=INFO \
    --hostname=store_randoms_in_redis_worker@%h \
    --autoscale=8,1 \
    --concurrency=8 \
    -Q store_randoms_in_redis_queue
;;

store-images-urls)
  exec celery \
    --app=monitoring_system.tasks.celery_utils:celery_app \
    worker \
    --loglevel=INFO \
    --hostname=store_images_urls@%h \
    --autoscale=8,1 \
    --concurrency=8 \
    -Q store_images_urls_queue
;;

beat)
exec celery \
     -A  monitoring_system.tasks.celery_utils:celery_beat_app \
      beat \
      -l debug \
;;

esac