from flask import Flask, jsonify
from ops import aiops, greenops
import psutil

app = Flask(_name_)

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().used / (1024 * 1024)  # MB
    energy_score = greenops.calculate_energy_score(cpu, mem)
    alert = aiops.check_anomaly(cpu, mem)
    
    result = {
        "cpu_usage": f"{cpu}%",
        "memory_usage": f"{mem:.2f} MB",
        "greenops_score": f"{energy_score}%",
        "aiops_alert": alert
    }
    return jsonify(result)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
