import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
import subprocess

def start_camera():
    cmd = "python New.py --webcam 0"  
    subprocess.Popen(cmd, shell=True)

def end_camera():
    pass

root = tk.Tk()
root.title("Drowsiness Detection")
root.geometry("1200x1000") 
bg_image = Image.open("backgroundimage.jpg")  # Replace "background_image.jpg" with your image file
bg_width, bg_height = bg_image.size
bg_ratio = bg_width / bg_height
root_width = 1300  # Assuming root width
root_height = int(root_width / bg_ratio)
root.geometry(f"{root_width}x{root_height}")

bg_image = bg_image.resize((root_width, root_height), Image.LANCZOS)

bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relx=0.5, rely=0.5, anchor="center")

# Create a style for buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)

# Create title label

title_banner = ttk.Label(root, text="PU HACKATHON 2024", font=('Arial', 16, 'bold'),padding=10)
title_banner.place(relx=0.62, rely=0.22, anchor="center")
title_label = ttk.Label(root, text="Drive Aware Alarm", font=('Arial', 16, 'bold'),padding=10)
title_label.place(relx=0.62, rely=0.3, anchor="center")

# Create start button with styling
start_button = ttk.Button(root, text="Start Camera", command=start_camera, style='TButton',padding=10)
start_button.place(relx=0.55, rely=0.5, anchor="center")

# Create end button with styling
end_button = ttk.Button(root, text="End Camera", command=end_camera, style='TButton')
end_button.place(relx=0.7, rely=0.5, anchor="center")

# Create a div for team information
team_div = tk.Frame(root)
team_div.place(relx=.7, rely=.75, anchor="e")

# Display team name
team_name_label = tk.Label(team_div, text="Code Cloners(PU031)", font=('Arial', 14, 'bold'),padx=10,pady=20)
team_name_label.pack()

# Display team members
team_members = ["Varun kumar", "Rohith kumar", "Surya vishnu", "Jagan Killi"]
for member in team_members:
    member_label = tk.Label(team_div, text=member, font=('Arial', 16, 'bold'), bg='white',padx=10,pady=10)  # Set background color to white and increase font size
    member_label.pack(anchor='center')
root.mainloop()