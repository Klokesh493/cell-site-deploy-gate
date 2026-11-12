# Cell Site Deploy Gate walkthrough

## Business problem

A maintenance change should be held when a site has active alarms, insufficient healthy neighbors, or no approved maintenance window.

## Reproduce the workflow

Run `python3 site_deploy_gate.py sample_sites.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
nyc-101 allow
chi-022 block
```

The sample supplies these fields. `site`, `maintenance_window`, `active_alarms`, `healthy_neighbors`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
