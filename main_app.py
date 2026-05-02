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
if __name__ == "__main__":  
    root = tk.Tk()
    app = ScholarSyncUI(root)
    root.mainloop()

      
    