import unittest
from logic import StudentManager

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()

        def test_timer_tick(self):
            self.manager.is_running = True
            self.manager.run_timer_tick()
            # This proves the math works (1500 - 1 = 1499
            self.assertEqual(self.manager.time_left, 1499)

if __name__ == '__main__':
 unittest.main() 