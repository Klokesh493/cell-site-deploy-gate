# Cell Site Deploy Gate

A maintenance change should be held when a site has active alarms, insufficient healthy neighbors, or no approved maintenance window.

## What I built

I built a telecom maintenance gate that checks for an approved window, zero active alarms, and at least two healthy neighbors. Each site receives an allow or block recommendation from its exported snapshot.

## How it works

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

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [site_deploy_gate.py](site_deploy_gate.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 site_deploy_gate.py sample_sites.csv
```

The NYC sample is allowed. The Chicago sample is blocked. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 site_deploy_gate.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

Use current site telemetry and change approvals before carrying out work. The CLI does not initiate a deployment.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
