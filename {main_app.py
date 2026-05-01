import tkinter as tk


from logic import StudentManager # This imports your logic.py file so you can use the StudentManager class and its methods in your UI.

class ScholarSyncUI:
  def __init__(self, root):
        self.root = root
        self.root.title("ScholarSync - Focus Hub    ")
        # This connects to your logic.py file
        # Initialize the "THhinking" part from logic.py
        self.manager = StudentManager()
        
        # UI Elements
        self.welcome_label = tk.Label(self.root, text="Welcome to ScholarSync!", font=("Arial", 16))
        self.welcome_label.pack(pady=20)
       
        self.timer_label = tk.Label(self.root, text="25:00", font=("Helvetica", 48), fg="white", bg="black")
        self.timer_label.pack(pady=10)
       
        self.start_button = tk.Button(self.root, text="Start Study Session", command=self.start_timer)
        self.start_button.pack(pady=10)

        
  def start_timer(self):
       self.manager.time_left = 1500  # Reset timer to 25 minutes
       self.manager.is_running = True
       self.update_gui_timer()  # Start the GUI timer updates
  def update_gui_timer(self): # 'dt' is a placeholder for the time delta that the logic.py might use for timing
      # Call the method from logic.py to subtract 1 second 
      if self.manager.run_timer_tick():  # This will return True if the timer is still running, False if it has finished
          # Call the method from logic.py to update the timer
          minutes, seconds = divmod(self.manager.time_left, 60) 
          time_format: str = f"{minutes:02d}:{seconds:02d}"
          
          self.timer_label.config(text=time_format)
          
          self.root.after(1000, self.update_gui_timer)  # Schedule the next update after 1 second
      
        
# This part Must be at the very bottom to launch the window
if __name__ == "__main__":  
    root = tk.Tk()
    app = ScholarSyncUI(root)
    root.mainloop()
      
    