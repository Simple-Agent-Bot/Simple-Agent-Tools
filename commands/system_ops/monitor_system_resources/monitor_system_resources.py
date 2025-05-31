import psutil

# Fetch system performance data such as CPU usage, memory usage, and disk utilization
def monitor_system_resources():
    return {
        'CPU Usage (%)': psutil.cpu_percent(interval=1),
        'Memory Usage (%)': psutil.virtual_memory().percent,
        'Disk Usage (%)': psutil.disk_usage('/').percent
    }

if __name__ == '__main__':
    print(monitor_system_resources())