import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

# Load the trained model to classify the images
from keras.models import load_model
model = load_model('model1_cifar_10epoch.h5')

# Dictionary to label all the CIFAR-10 dataset classes
classes = { 
    0: 'aeroplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck'
}

# Initialize GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Image Classification CIFAR10')
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

def classify(file_path):
    """
    Classify the uploaded image using the trained model.
    """
    global label_packed
    try:
        # Preprocess the image
        image = Image.open(file_path)
        image = image.resize((32, 32))  # Resize to (32, 32, 3)
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        image = np.array(image).astype('float32') / 255.0  # Normalize and convert to float32
        
        # Debugging: Print image shape
        print(f"Image shape: {image.shape}")
        
        # Predict using the model
        pred = model.predict(image)  # Get predictions
        predicted_class = np.argmax(pred, axis=1)[0]  # Extract class index
        sign = classes[predicted_class]  # Map to class label
        
        # Debugging: Print prediction probabilities
        print(f"Prediction probabilities: {pred}")
        print(f"Predicted class: {sign}")
        
        # Update label with prediction result
        label.configure(foreground='#011638', text=sign)
    except Exception as e:
        print(f"Error during classification: {e}")

def show_classify_button(file_path):
    """
    Show the 'Classify Image' button after an image is uploaded.
    """
    classify_b = Button(top, text="Classify Image",
                        command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white',
                         font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def upload_image():
    """
    Allow user to upload an image for classification.
    """
    try:
        file_path = filedialog.askopenfilename()
        if not file_path:
            return  # If user cancels, do nothing
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25),
                            (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except Exception as e:
        print(f"Error during image upload: {e}")

# GUI Layout
upload = Button(top, text="Upload an image", command=upload_image,
                padx=10, pady=5)
upload.configure(background='#364156', foreground='white',
                 font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)

sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)

heading = Label(top, text="Image Classification CIFAR10", pady=20,
                font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
