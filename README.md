# rabbitmq-exporter

[Prometheus](https://prometheus.io/) exporter for [RabbitMQ](https://rabbitmq.com/).

```bash
# Run RabbitMQ
$ docker run -d --name rabbitmq -p 15672:15672 rabbitmq:3-management

# Run rabbitmq-exporter
$ docker run -d --name rabbitmq-exporter -p 9095:9095 --link rabbitmq \
    -e RMQ_HOST=http://rabbitmq:15672 -e RMQ_USER=guest -e RMQ_PASSWORD=guest \
    ghcr.io/adrianchifor/rabbitmq-exporter:latest

$ curl localhost:9095/metrics | grep rmq

# HELP rmq_messages_total Number of messages in queue
# TYPE rmq_messages_total gauge
# HELP rmq_exchanges_total Number of exchanges
# TYPE rmq_exchanges_total gauge
rmq_exchanges_total{node="rabbit@8fa13dcf2b6a"} 7.0
# HELP rmq_queues_total Number of queues
# TYPE rmq_queues_total gauge
rmq_queues_total{node="rabbit@8fa13dcf2b6a"} 0.0
# HELP rmq_consumers_total Number of consumers
# TYPE rmq_consumers_total gauge
rmq_consumers_total{node="rabbit@8fa13dcf2b6a"} 0.0
# HELP rmq_connections_total Number of connections
# TYPE rmq_connections_total gauge
rmq_connections_total{node="rabbit@8fa13dcf2b6a"} 0.0
# HELP rmq_channels_total Number of channels
# TYPE rmq_channels_total gauge
rmq_channels_total{node="rabbit@8fa13dcf2b6a"} 0.0
# HELP rmq_mem_used Memory used
# TYPE rmq_mem_used gauge
rmq_mem_used{node="rabbit@8fa13dcf2b6a"} 1.07061248e+08
# HELP rmq_mem_limit Memory limit
# TYPE rmq_mem_limit gauge
rmq_mem_limit{node="rabbit@8fa13dcf2b6a"} 8.35282534e+08
# HELP rmq_mem_alarm Memory alarm status
# TYPE rmq_mem_alarm gauge
rmq_mem_alarm{node="rabbit@8fa13dcf2b6a"} 0.0
# HELP rmq_disk_free Disk free space
# TYPE rmq_disk_free gauge
rmq_disk_free{node="rabbit@8fa13dcf2b6a"} 9.20752128e+08
# HELP rmq_disk_free_limit Disk limit
# TYPE rmq_disk_free_limit gauge
rmq_disk_free_limit{node="rabbit@8fa13dcf2b6a"} 5e+07
# HELP rmq_disk_free_alarm Disk alarm status
# TYPE rmq_disk_free_alarm gauge
rmq_disk_free_alarm{node="rabbit@8fa13dcf2b6a"} 0.0
# HELP rmq_socket_used Used sockets
# TYPE rmq_socket_used gauge
rmq_socket_used{node="rabbit@8fa13dcf2b6a"} 0.0
# HELP rmq_socket_limit Sockets limit
# TYPE rmq_socket_limit gauge
rmq_socket_limit{node="rabbit@8fa13dcf2b6a"} 943629.0
# HELP rmq_fd_used File descriptors used
# TYPE rmq_fd_used gauge
rmq_fd_used{node="rabbit@8fa13dcf2b6a"} 33.0
# HELP rmq_fd_limit File descriptors limit
# TYPE rmq_fd_limit gauge
rmq_fd_limit{node="rabbit@8fa13dcf2b6a"} 1.048576e+06
# HELP rmq_running Node is running
# TYPE rmq_running gauge
rmq_running{node="rabbit@8fa13dcf2b6a"} 1.0
```
