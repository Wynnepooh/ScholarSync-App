class StudentManager: 
    def __init__(self, study_resources=None):
        self.study_resources = study_resources or ["https://google.com", "https://facebook.com", "https://twitter.com"]
        self.time_left = 1500 # 25 minutes in seconds
        self.is_running = False
    
    def run_timer_tick(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            return True
        else:
            return False
            




