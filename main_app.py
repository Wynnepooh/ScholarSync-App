import tkinter as tk


from logic import StudentManager # This imports your logic.py file so you can use the StudentManager class and its methods in your UI.

class ScholarSyncUI:
  def __init__(self, root):
        self.root = root
        self.root.title("ScholarSync - Focus Hub    ")
        self.root
        # This connects to your logic.py file
        # Initialize the "THhinking" part from logic.py
        self.manager = StudentManager()
        
        # UI Elements
        self.label = tk.Label(root, text="Welcome to ScholarSync!", font=("Arial", 16))
        self.label.pack(pady=20)
       
        self.btn = tk.Button(root, text="Show Study Links", command=self.display_links)
        self.btn.pack(pady=10)
        
        # output area to show results in the window
        self.output_label = tk.Label(root, text="", wraplength=350)
        self.timer_label = tk.Label(root, text="25:00", font=("Arial", 24), fg="red")
        self.timer_label.pack(pady=20)
        self.update_timer()
  def display_links(self):
        # This calls the logic from your logic.py
        links = self.manager.get_links_student()
        
        # Join the list into a string to show in the UI
        links_str = "\n".join(links)
        print(f"Loading resources: {links_str}")
       
        self.output_label.config(text=f"Resources Found:\n{links_str}")
        print(f"Terminal Log: {links}")
  
  def update_timer(self):
       
        time_string = self.manager.format_time()

        self.timer_label.config(text=time_string)

        if self.manager.run_timer_tick():
             self.root.after(1000, self.update_timer)

        # This part Must be at the very bottom to launch the window
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

      
    