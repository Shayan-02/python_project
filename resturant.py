import tkinter as tk
from tkinter import messagebox


# Function to calculate total
def calculate_total():
    total = 0
    for item, price in menu_items.items():
        qty = quantities[item].get()
        total += price * qty
    total_label.config(text=f"Total: ${total:.2f}")


# Function to place order
def place_order():
    orders = {
        item: quantities[item].get()
        for item in menu_items
        if quantities[item].get() > 0
    }
    if orders:
        order_details = "\n".join([f"{item}: {qty}" for item, qty in orders.items()])
        messagebox.showinfo("Order Placed", f"Your order:\n{order_details}\nThank you!")
        reset_fields()
    else:
        messagebox.showwarning("No Order", "Please add items to the order.")


# Function to reset fields
def reset_fields():
    for item in menu_items:
        quantities[item].set(0)
    calculate_total()


# Menu items with prices
menu_items = {
    "Pizza": 12.99,
    "Burger": 8.99,
    "Pasta": 10.99,
    "Salad": 6.99,
    "Soda": 1.99,
}

# Tkinter window setup
root = tk.Tk()
root.title("Restaurant Order System")
root.geometry("400x400")

# GUI Elements
title_label = tk.Label(root, text="Restaurant Menu", font=("Helvetica", 16))
title_label.pack()

quantities = {}
for item, price in menu_items.items():
    frame = tk.Frame(root)
    frame.pack(pady=5)
    label = tk.Label(frame, text=f"{item} (${price:.2f}):")
    label.pack(side="left")
    quantities[item] = tk.IntVar(value=0)
    spinbox = tk.Spinbox(frame, from_=0, to=10, textvariable=quantities[item], width=5)
    spinbox.pack(side="right")

total_label = tk.Label(root, text="Total: $0.00", font=("Helvetica", 14))
total_label.pack(pady=10)

calc_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calc_button.pack(pady=5)

order_button = tk.Button(root, text="Place Order", command=place_order)
order_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack(pady=5)

root.mainloop()
