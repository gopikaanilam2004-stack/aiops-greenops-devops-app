def check_anomaly(cpu, mem):
    alerts = []
    if cpu > 75:
        alerts.append(f"⚠ High CPU spike detected: {cpu}%")
    if mem > 500:  # MB
        alerts.append(f"⚠ High Memory usage detected: {mem:.2f} MB")
    return alerts if alerts else "✅ All metrics normal"
