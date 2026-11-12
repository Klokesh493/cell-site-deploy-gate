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

## Business problem

A maintenance change should be held when a site has active alarms, insufficient healthy neighbors, or no approved maintenance window.

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

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 site_deploy_gate.py sample_sites.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)
