#!/bin/bash\ncurl -X POST http://localhost:3000/api/dashboards/db -H "Content-Type: application/json" -d @grafana-dashboard.json
