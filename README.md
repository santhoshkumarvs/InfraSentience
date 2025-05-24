📦 Project 1: InfraSentience
🎯 Purpose
InfraSentience simulates a modern MLOps inference pipeline powered by:

FastAPI for inference serving

Triton Inference Server (simulated)

Prometheus + Grafana for monitoring

GitHub Actions for CI/CD automation

This project is geared towards infrastructure-level simulation of scalable, production-grade ML deployments.

InfraSentience/
│
├── src/
│   └── main.py                     # FastAPI app with /simulate endpoint, logs + Prometheus
│
├── tests/
│   └── test_simulation.py          # Unit test stub
│
├── pipelines/
│   └── cost_aware_pipeline.md      # Simulated cost-aware pipeline description
│
├── observability/
│   └── llmops_metrics.md           # Notes on LLMOps observability metrics
│
├── monitoring/
│   ├── prometheus-config.yaml      # Prometheus configuration for metrics scraping
│   └── grafana-dashboard.json      # Example Grafana dashboard visualization
│
├── triton_server/
│   └── model_repository/
│       └── sample_model/
│           └── config.pbtxt        # Simulated model config for Triton Inference Server
│
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml      # GitHub Actions CI config
│
├── Dockerfile                      # Docker setup for FastAPI app
├── docker-compose.yml              # Full stack: app, Prometheus, Grafana
├── requirements.txt                # Python deps for app
├── README.md                       # Project info
├── deploy_config.yaml              # Placeholder config file
├── demo.sh                         # Test script for /simulate endpoint
└── git_push.sh                     # GitHub automation script
