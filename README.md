# Monitoring System

This Git repository represents a monitoring system that integrates various free services, including Grafana, Prometheus, Celery Workers, Celery Beat, Redis, PostgreSQL, RabbitMQ, and Celery Flower.

## System Activation

To activate the monitoring system, run the following command in the console:

```bash
./build.sh make
```

This command will automatically build and start the system. Docker and Docker Compose logs will be displayed on the screen.

## Stopping the System

To stop the monitoring system, simply press any key, and the system will shut down gracefully using `docker compose down`.

## Services Included

- **Grafana:** Metrics visualization and monitoring dashboard.
- **Prometheus:** Monitoring and alerting toolkit.
- **Celery Workers:** Various Celery workers (store-randoms-in-file-worker, store-randoms-in-redis-worker, store-images-urls, celery-beat).
- **Redis:** Key-value store and cache.
- **PostgreSQL:** Database for storing tasks and data.
- **RabbitMQ:** Message broker for Celery workers.
- **Celery Flower:** Real-time Celery monitoring tool.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KnollYehuda/monitoring-system.git
   cd monitoring-system
   ```

2. **Activate the system:**

   ```bash
   ./build.sh make
   ```

3. **Access services:**

   - Grafana: [http://localhost:3000](http://localhost:3000) (default credentials: admin/admin)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - Celery Flower: [http://localhost:5555](http://localhost:5555)

4. **Stop the system:**

   - Press any key in the console.
   - ./build.sh make down

## Configuration

- Customize the Docker Compose configuration in `docker-compose.yml` for service configurations.
- Adjust the Makefile as needed for specific project requirements.
