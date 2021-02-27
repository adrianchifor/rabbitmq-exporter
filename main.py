import os
import time
import logging
import requests
import metrics

from prometheus_client import start_http_server

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] - %(message)s")
log = logging.getLogger("rabbitmq-exporter")

RMQ_HOST = os.getenv("RMQ_HOST", "http://localhost:15672")
RMQ_USER = os.getenv("RMQ_USER", "guest")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD", "guest")
METRICS_PORT = int(os.getenv("METRICS_PORT", 9095))


def get_stats(endpoint: str):
    response = requests.get(f"{RMQ_HOST}/api/{endpoint}", auth=(RMQ_USER, RMQ_PASSWORD), timeout=5)
    assert response.status_code == 200
    return response.json()


def get_queues():
    for queue in get_stats("queues"):
        metrics.msgs_total.labels(queue["name"]).set(queue["backing_queue_status"]["len"])


def get_nodes():
    for node in get_stats("nodes"):
        if not node["running"]:
            metrics.running.labels(node["name"]).set(0)
        else:
            metrics.mem_used.labels(node["name"]).set(node["mem_used"])
            metrics.mem_limit.labels(node["name"]).set(node["mem_limit"])
            if node["mem_alarm"]:
                metrics.mem_alarm.labels(node["name"]).set(1)
            else:
                metrics.mem_alarm.labels(node["name"]).set(0)
            metrics.disk_free.labels(node["name"]).set(node["disk_free"])
            metrics.disk_free_limit.labels(node["name"]).set(node["disk_free_limit"])
            if node["disk_free_alarm"]:
                metrics.disk_free_alarm.labels(node["name"]).set(1)
            else:
                metrics.disk_free_alarm.labels(node["name"]).set(0)
            metrics.socket_used.labels(node["name"]).set(node["sockets_used"])
            metrics.socket_limit.labels(node["name"]).set(node["sockets_total"])
            metrics.fd_used.labels(node["name"]).set(node["fd_used"])
            metrics.fd_limit.labels(node["name"]).set(node["fd_total"])
            metrics.running.labels(node["name"]).set(1)


def get_overview():
    json = get_stats("overview")
    obj = json["object_totals"]
    metrics.exchanges_total.labels(json["node"]).set(obj["exchanges"])
    metrics.queues_total.labels(json["node"]).set(obj["queues"])
    metrics.consumers_total.labels(json["node"]).set(obj["consumers"])
    metrics.conns_total.labels(json["node"]).set(obj["connections"])
    metrics.channels_total.labels(json["node"]).set(obj["channels"])


def collect_metrics():
    try:
        get_queues()
        get_nodes()
        get_overview()
    except Exception:
        log.error("Failed to collect RabbitMQ metrics", exc_info=True)


if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    log.info(f"Running Prometheus metrics server on port {METRICS_PORT}")

    while True:
        log.info(f"Collecting metrics from {RMQ_HOST}")
        collect_metrics()
        time.sleep(float(os.getenv("COLLECT_INTERVAL", 30.0)))
