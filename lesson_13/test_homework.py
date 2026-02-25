import os
import unittest
from lesson_13.homework import log_event

class TestLogging(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        if os.path.exists('login_system.log'):
            try:
                with open('login_system.log', 'w'):
                    pass
            except PermissionError:
                print("\n File was blocked.")

    def test_log_success(self):
        with self.assertLogs('log_event', level='INFO') as captured_logs:
            log_event("user1", "success")

        # format check
        self.assertIn("INFO:log_event:Login event - Username: user1, Status: success", captured_logs.output[0])

    def test_log_expired(self):
        with self.assertLogs('log_event', level='WARNING') as captured_logs:
            log_event("hacker", "expired")

        # format check
        self.assertIn("WARNING:log_event:Login event - Username: hacker, Status: expired", captured_logs.output[0])

    def test_log_failed(self):
        with self.assertLogs('log_event', level='ERROR') as captured_logs:
            log_event("user2", "failed")

        # format check
        self.assertIn("ERROR:log_event:Login event - Username: user2, Status: failed", captured_logs.output[0])

    def test_log_unknown_status(self):
        with self.assertLogs('log_event', level='ERROR') as captured_logs:
            log_event("guest", "unknown")

        # format check
        self.assertIn("ERROR:log_event:Login event - Username: guest, Status: unknown", captured_logs.output[0])


if __name__ == '__main__':
    unittest.main()