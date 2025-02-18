from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import tkinter as tk
from PIL import Image, ImageTk
import io

# Set Firefox options
binary = r"C:\Program Files\Mozilla Firefox\firefox.exe"
options = Options()
options.accept_insecure_certs = False
options.binary_location = binary
options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.http", "localhost")
options.set_preference("network.proxy.http_port", 3128)
options.add_argument("-headless")  # Run headless

# Initialize driver with options
driver = webdriver.Firefox(options=options)

def open_funeral_image():
    image_url = "https://scontent-mia3-3.xx.fbcdn.net/v/t39.30808-6/480238348_1426114441843518_6590070147334309770_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=mZHnMhV8i6sQ7kNvgERB27b&_nc_oc=AdjJtA16i2pVVYedygkDn0YccndCRkYUyzRetVouvBV2YPOBMObNZip249cASn7l0oU&_nc_zt=23&_nc_ht=scontent-mia3-3.xx&_nc_gid=AR1F7vgd8dOHA52rr1I8SDn&oh=00_AYC65wc2LaAdW6blTYUsr3t-Ub8G7R9zS6TmCUm_5lYFbg&oe=67BA75D8"
    driver.get(image_url)

    # Capture screenshot of the web page
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(screenshot))

    # Create Tkinter GUI window
    root = tk.Tk()
    root.title("Memorial")

    # Overlay "Rest in Peace" text on the screenshot
    label = tk.Label(root, text="Rest in Peace", font=("Helvetica", 24), fg="white", bg="black")
    label.pack(fill=tk.X, padx=10, pady=10)

    # Add the second line of text
    second_label = tk.Label(root, text="The true crypto GOAT: Tesla and Apple will never recover", font=("Helvetica", 16), fg="white", bg="black")
    second_label.pack(fill=tk.X, padx=10, pady=10)

    # Convert screenshot to Tkinter-compatible image and display it
    tk_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(root, width=image.width, height=image.height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    # Keep the GUI window open
    root.mainloop()

open_funeral_image()
