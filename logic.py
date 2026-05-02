class StudentManager: 
    def __init__(self):
        self.study_resources = ["https://google.com", "https://facebook.com", "https://twitter.com"]
        self.time_left = 25 * 60  # Default Pomodoro time in seconds (25 minutes)
        self.is_running = True

    def get_links_student(self):
        """Returns the list of resources to the student."""
        print("Logic: Fetching ressources...") # Helps you see it working in the terminal
        return self.study_resources
    
    def run_timer_tick(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            return True
        else:
            return False
            
    def format_time(self):
        
      

        
        mins, secs =divmod(self.time_left, 60)
        return f"{mins:02d}:{secs:02d}"
     
        
