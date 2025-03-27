

import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk  # Install using: pip install pillow

# Dictionary to store item images (Use your own image file paths)
item_images = {
    "Clothing": "images/clothing.jpg",
    "Footwear": "images/footwear.jpg",
    "Electronics": "images/electronics.jpg",
    "Home Appliances": "images/home_appliances.jpg",
    "Accessories": "images/accessories.jpg",
    "Books and note": "images/books.jpg",
    "Beauty Products": "images/beauty.jpg",
    "Snack": "images/snack.jpg",
    "Oil": "images/oil.jpg",
    "Juice": "images/juice.jpg",
    "Nuts": "images/nuts.jpg",
    "Vegetable and Fruits": "images/vegetables.jpg"
}

def show_item_image(item):
    """ Opens a new window to display the selected item's image. """
    if item not in item_images:
        messagebox.showerror("Error", f"No image found for {item}.")
        return

    image_path = item_images[item]

    try:
        # Open image window
        img_window = Toplevel()
        img_window.title(f"{item} Image")
        img_window.geometry("400x400")
        img_window.configure(bg="white")

        # Load and display the image
        img = Image.open(image_path)
        img = img.resize((300, 300))  # Resize image
        img = ImageTk.PhotoImage(img)

        label = tk.Label(img_window, image=img, bg="white")
        label.image = img  # Keep reference to avoid garbage collection
        label.pack(pady=10)

        # Label to show item name
        tk.Label(img_window, text=item, font=("Arial", 14, "bold"), bg="white").pack(pady=5)

    except Exception as e:
        messagebox.showerror("Image Error", f"Error loading image: {e}")

def open_items_page():
    """ Creates a new window for the items menu. """
    items_window = tk.Tk()
    items_window.title("Department Store Items")
    items_window.geometry("900x800")
    items_window.configure(bg="lightblue")

    # Create a menu bar
    menubar = tk.Menu(items_window)
    
    # Create a cascade menu for items
    items_menu = tk.Menu(menubar, tearoff=0)

    # List of store items
    items = list(item_images.keys())

    # Add each item as a menu command
    for item in items:
        items_menu.add_command(label=item, command=lambda i=item: show_item_image(i))
    
    # Add the items menu to the menu bar
    menubar.add_cascade(label="Items", menu=items_menu)
    
    # Configure the window to display the menu bar
    items_window.config(menu=menubar)

    # Welcome label
    tk.Label(items_window, text="Welcome to the Department Store Items Page", 
             font=("Arial", 16), bg="lightblue").pack(pady=20)

    items_window.mainloop()

def login():
    """ Handles the login and opens the items page. """
    messagebox.showinfo("Login Successful", "Welcome to the Department Store System!")
    root.destroy()  # Close the login window
    open_items_page()  # Open the items page with images

# Create the login window
root = tk.Tk()
root.title("Department Store Login")
root.geometry("400x250")
root.configure(bg="#D3D3D3")

# Title Label
tk.Label(root, text="Department Store Login", font=("Arial", 16, "bold"), bg="#D3D3D3").pack(pady=10)

# Username Label and Entry
tk.Label(root, text="Username:", font=("Arial", 12), bg="#D3D3D3").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password Label and Entry
tk.Label(root, text="Password:", font=("Arial", 12), bg="#D3D3D3").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login Button
tk.Button(root, text="Login", command=login, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()
