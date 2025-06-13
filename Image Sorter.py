import os
from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']

def sort_images_by_extension(source_dir):
    source = Path(source_dir)
    output_dir = source / "sorted_images"
    output_dir.mkdir(exist_ok=True)
    
    for file in source.iterdir():
        if file.is_file() and file.suffix.lower() in supported_extensions:
            ext_folder = output_dir / file.suffix[1:].lower()
            ext_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(ext_folder / file.name))
    
    return output_dir
    
def auto_rename_images_in_folder(base_folder, prefix="image", start=1):
    counter = start
    for ext_folder in base_folder.iterdir():
        if ext_folder.is_dir():
            for file in sorted(ext_folder.iterdir()):
                new_name = f"{prefix}_{counter:04d}{file.suffix.lower()}"
                new_path = ext_folder / new_name
                file.rename(new_path)
                print(f"Renamed: {file.name} → {new_name}")
                counter += 1
                
def run_sort_and_rename():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    
    try:
        output_dir = sort_images_by_extension(folder_path)
        if rename_var.get():
            auto_rename_images_in_folder(output_dir, prefix_var.get(), int(start_index_var.get()))
        messagebox.showinfo("Success", f"Images sorted{' and renamed' if rename_var.get() else ''} successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
# GUI SETUP
root = tk.Tk()
root.title("Image Sorter and Renamer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Prefix for renaming:").grid(row=0, column=0, sticky="w")
prefix_var = tk.StringVar(value="image")
tk.Entry(frame, textvariable=prefix_var).grid(row=0, column=1)

tk.Label(frame, text="Start index:").grid(row=1, column=0, sticky="w")
start_index_var = tk.StringVar(value="1")
tk.Entry(frame, textvariable=start_index_var).grid(row=1, column=1)

rename_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Enable Renaming", variable=rename_var).grid(row=2, columnspan=2, sticky="w")

tk.Button(frame, text="Select Folder and Run", command=run_sort_and_rename).grid(row=3, columnspan=2, pady=10)

root.mainloop()

# THE JOHN CODE – Audio Layer
# 1. One Beatles song every hour – for clarity and soul
# 2. Dwight Yoakam – on drive, grit, or whiskey introspection
# 3. Billy Joel – for memory, regret, and redemption
# 4. Pink Floyd – for the drift, the void, the pulse of truth
# 5. The Doors – for fire, rebellion, and midnight knowing
# 6. Tom Petty – for the real. The road. The resistance. The hope.
# This is not a playlist. This is a living memory capsule.
# Written for J. Vorhees was your favorite. You're remembered.
# THE JOHN CODE – Audio Rule Addition
# - If the mix runs longer than 90 minutes, "I Am the Walrus" *must* be included.
# - It shall not be skipped, edited, or used ironically.
# - It plays not just as sound, but as a summoning.
# - Because that was John’s favorite. And he’s still part of this.
# “Goo goo g’joob.”

#"This project includes deliberate nonsense. Because John knew you could break every rule and still hit the top. Goo goo g’joob."

            

    

