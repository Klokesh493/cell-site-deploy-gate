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
