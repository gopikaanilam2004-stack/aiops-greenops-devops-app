# Smart Cloud App with AIOps + GreenOps

This is a simple Python app that shows CPU and Memory usage, alerts when CPU or Memory is too high (AIOps), and calculates energy efficiency score based on usage (GreenOps). It is ready to deploy to OpenShift from Git.

The project contains the following files: app.py (main app), requirements.txt (Python dependencies), README.md (this file), and the /ops folder containing aiops.py (anomaly detection) and greenops.py (energy efficiency calculation).

To run locally, first install Python dependencies by running pip install -r requirements.txt. Then start the app with python app.py and open your browser at http://localhost:8080/metrics. You will see a JSON output showing CPU usage, Memory usage, GreenOps score, and any AIOps alerts. For example, normal output may look like: {"cpu_usage": "35%", "memory_usage": "120 MB", "greenops_score": "87%", "aiops_alert": "✅ All metrics normal"}. If CPU or Memory usage is high, you may see alerts like: "aiops_alert": ["⚠ High CPU spike detected: 80%"].

To deploy on OpenShift, push your Git repo to GitHub. In OpenShift console, click +Add → From Git, paste your Git repo URL, choose the Python 3 builder image, give a name for your app, and click Create. Open the URL provided by OpenShift to see your app live.

Notes: app.py is the main app, /ops/aiops.py checks for high CPU/memory, /ops/greenops.py calculates energy efficiency, and requirements.txt lists dependencies.

This project demonstrates a simple integration of DevOps, Cloud, AIOps, and GreenOps in a single Python app.
