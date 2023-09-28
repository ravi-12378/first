import tkinter as tk
import pyshorteners

def shorten_url():
    original_url = original_url_entry.get()
    if original_url:
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(original_url)
            short_url_label.config(text="Short URL: " + short_url)
        except Exception as e:
            short_url_label.config(text="Error: " + str(e))
    else:
        short_url_label.config(text="Enter a valid URL")

# Create a Tkinter window
window = tk.Tk()
window.title("URL Shortener")

# Create and pack GUI elements
original_url_label = tk.Label(window, text="Enter URL:")
original_url_label.pack()

original_url_entry = tk.Entry(window)
original_url_entry.pack()

shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack()

short_url_label = tk.Label(window, text="")
short_url_label.pack()

# Start the Tkinter main loop
window.mainloop()
