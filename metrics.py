from prometheus_client import Gauge

msgs_total = Gauge("rmq_messages_total", "Number of messages in queue", ["queue"])
exchanges_total = Gauge("rmq_exchanges_total", "Number of exchanges", ["node"])
queues_total = Gauge("rmq_queues_total", "Number of queues", ["node"])
consumers_total = Gauge("rmq_consumers_total", "Number of consumers", ["node"])
conns_total = Gauge("rmq_connections_total", "Number of connections", ["node"])
channels_total = Gauge("rmq_channels_total", "Number of channels", ["node"])

mem_used = Gauge("rmq_mem_used", "Memory used", ["node"])
mem_limit = Gauge("rmq_mem_limit", "Memory limit", ["node"])
mem_alarm = Gauge("rmq_mem_alarm", "Memory alarm status", ["node"])
disk_free = Gauge("rmq_disk_free", "Disk free space", ["node"])
disk_free_limit = Gauge("rmq_disk_free_limit", "Disk limit", ["node"])
disk_free_alarm = Gauge("rmq_disk_free_alarm", "Disk alarm status", ["node"])
socket_used = Gauge("rmq_socket_used", "Used sockets", ["node"])
socket_limit = Gauge("rmq_socket_limit", "Sockets limit", ["node"])
fd_used = Gauge("rmq_fd_used", "File descriptors used", ["node"])
fd_limit = Gauge("rmq_fd_limit", "File descriptors limit", ["node"])

running = Gauge("rmq_running", "Node is running", ["node"])
