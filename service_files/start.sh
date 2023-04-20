
# build monitoring system image
docker build --target monitoring-system -t monitoring-system .

# start services
docker compose up -d
