import time
import random

while True:
    throughput = random.randint(50, 300)
    latency = round(random.uniform(0.2, 1.0), 3)
    saturation = round(random.uniform(0.5, 0.9), 2)
    print(f"LLMOps Metrics - Throughput: {throughput}, Latency: {latency}, Saturation: {saturation}")
    time.sleep(5)
