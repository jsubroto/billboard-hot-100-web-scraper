import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk

def open_csv():
    """Opens a CSV file and displays it in a Treeview."""

    filepath = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )

    if filepath:
        try:
            df = pd.read_csv(filepath)
            display_data(df)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to open file:\n{e}")

def display_data(df):
    """Displays the DataFrame in a Treeview."""

    # Create a new window for the data
    data_window = tk.Toplevel(root)
    data_window.title("CSV Data")

    # Create a Treeview widget
    tree = ttk.Treeview(data_window, columns=df.columns.tolist(), show="headings")

    # Set column headings
    for col in df.columns:
        tree.heading(col, text=col)

    # Insert data into the Treeview
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=row.tolist())

    # Pack the Treeview
    tree.pack(expand=True, fill="both")

root = tk.Tk()
root.title("CSV Viewer")

open_button = tk.Button(root, text="Open CSV File", command=open_csv)
open_button.pack(pady=20)

root.mainloop()