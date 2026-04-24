from logic import StudentManager

def test_my_timer():

    manager = StudentManager()
    manager.is_running = True


    manager.run_timer_tick()


    if manager.time_left == 1499:
        print("Test Passed: The timer counted down!")
    else:
        print(f"Test Failed: Expected 1499, but got {manager.time_left}")

test_my_timer()