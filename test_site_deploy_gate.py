import unittest

from site_deploy_gate import decision


class SiteDeployGateTest(unittest.TestCase):
    def test_blocks_outside_window(self):
        row = {"site": "chi", "maintenance_window": "no", "active_alarms": "0", "healthy_neighbors": "4"}
        self.assertEqual(decision(row), "block")


if __name__ == "__main__":
    unittest.main()
