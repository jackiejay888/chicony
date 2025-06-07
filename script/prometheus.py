from flask import Flask, Response
from prometheus_client import generate_latest, Counter, Gauge
import random

app = Flask(__name__)

requests_total = Counter('my_app_requests_total', 'Total number of requests made to my application.')

random_value_gauge = Gauge('my_app_random_value', 'A random value to demonstrate gauge.')

@app.route('/metrics')
def metrics():
    requests_total.inc()

    random_value_gauge.set(random.uniform(0, 100))

    return Response(generate_latest(), mimetype='text/plain; version=0.0.4; charset=utf-8')

@app.route('/healthz')
def healthz():
    return "OK", 200

if __name__ == '__main__':
    print("Prometheus 指標匯出器已啟動，請在 http://127.0.0.1:8000/metrics 訪問指標")
    print("健康檢查端點請訪問 http://127.0.0.1:8000/healthz")
    app.run(host='0.0.0.0', port=8000)