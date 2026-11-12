# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 site_deploy_gate.py sample_sites.csv
nyc-101 allow
chi-022 block
test_blocks_outside_window (test_site_deploy_gate.SiteDeployGateTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
