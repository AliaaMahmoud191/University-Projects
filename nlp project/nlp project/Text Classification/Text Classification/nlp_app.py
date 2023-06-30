import tkinter as tk
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from langdetect import detect
#nltk.download('stopwords')


model = None
cv = None

def check_text(text):
    try:
        lang = detect(text)
        return lang == 'en'
    except:
        return False

def process_text():
    
    input_text = text_input.get("1.0", "end-1c")  # Get the text from the text input field
    
    if check_text(input_text):
        output_label.config(text=predict(input_text))  # Update the output label with the input text
    else:
        output_label.config(text="Input text is invalid")  # Output an error message

def load_model():
    # Load the saved model and CountVectorizer instance, we will use this at the python app 
    global model , cv
    
    with open('./model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('./cv.pkl', 'rb') as f:
        cv = pickle.load(f)
    
def predict(text):
    categories = ['World','Sports','Business','Sci/Tech']
    ps = PorterStemmer()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)

    text_X = cv.transform([text]).toarray()

    preds = model.predict(text_X)
    print(preds)
    result = categories[preds[0]]
    return f"Category : {result}"
   
    
# Create the main window
root = tk.Tk()
root.title("Article Classifier")
root.geometry("500x500")
root["background"] ="#0C134F"
load_model()

canvas = tk.Canvas(root, bg="#0C134F")
canvas.pack(fill="both", expand=True)

# Create the input label and text field
input_label = tk.Label(canvas, text="Article Classifier", pady=10, font=("Helvetica", 20, "bold"), bg="#0C134F", fg="white")
input_label.pack(fill="both", expand=True, pady=10)

text_input = tk.Text(canvas, height=15, width=45, font=("Helvetica", 12))
text_input.pack(pady=10, expand=True)

# Create the button to process the input text
process_button = tk.Button(canvas, text="Classify Text", font=("Helvetica", 12, "bold"), command=process_text,bg="blue", fg="white")
process_button.pack(expand=True, pady=5)

# Create the output label
output_label = tk.Label(canvas, text="", padx=20, pady=20, font=("Helvetica", 14, "bold"), bg = "#0C134F", fg="cyan")
output_label.pack(expand=True)

# Start the GUI loop
root.mainloop()
