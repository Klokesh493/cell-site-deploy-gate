# Cell Site Deploy Gate

Blocks site deployments when maintenance windows, alarms, or neighbor-cell health are unsafe.

Focus: Telecom DevOps deployment safety.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 site_deploy_gate.py sample_sites.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

```mermaid
flowchart LR
    A["Site maintenance snapshot"]
    B["Check maintenance window, active alarms, and healthy neighbors"]
    C{"All three gates pass?"}
    D["Allow deployment recommendation"]
    E["Block deployment recommendation"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
