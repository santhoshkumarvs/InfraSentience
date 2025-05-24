import time, random
while True:
    latency = random.uniform(0.1, 1.5)
    print(f"[SLA Monitor] Current latency: {latency}")
    if latency > 1.0:
        print("ALERT: SLA violation in InfraSentience detected.")
    time.sleep(6)
