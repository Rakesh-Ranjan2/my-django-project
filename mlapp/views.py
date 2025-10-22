from django.shortcuts import render
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
from PIL import Image




# Load model once when server starts
model = load_model('mlapp/prototype1.h5')

class_names  = [
  'Apple ➔  Apple scab',
  'Apple ➔  Black rot',
  'Apple ➔  Cedar apple rust',
  'Apple ➔  healthy',
  'Blueberry ➔  healthy',
  'Cherry ➔ Powdery mildew',
  'Cherry (including sour) ➔ healthy',
  'Corn (maize) ➔  Cercospora leaf spot Gray leaf spot',
  'Corn (maize) ➔  Common rust ',
  'Corn (maize) ➔  Northern Leaf Blight',
  'Corn (maize) ➔  healthy',
  'Grape ➔  Black rot',
  'Grape ➔  Esca (Black Measles)',
  'Grape ➔  Leaf blight (Isariopsis Leaf Spot)',
  'Grape ➔  healthy',
  'Orange ➔  Haunglongbing (Citrus greening)',
  'Peach ➔  Bacterial spot',
  'Peach ➔  healthy',
  'Bell Pepper ➔ Bacterial spot',
  'Bell Pepper ➔ healthy',
  'Potato ➔ Early blight',
  'Potato ➔ Late blight',
  'Potato ➔ healthy',
  'Raspberry ➔ healthy',
  'Soybean ➔ healthy',
  'Squash ➔ Powdery mildew',
  'Strawberry ➔ Leaf scorch',
  'Strawberry ➔ healthy',
  'Tomato ➔ Bacterial spot',
  'Tomato ➔ Early blight',
  'Tomato ➔ Late blight',
  'Tomato ➔ Leaf Mold',
  'Tomato ➔ Septoria leaf spot',
  'Tomato ➔ Spider mites Two-spotted spider mite',
  'Tomato ➔ Target Spot',
  'Tomato ➔ Tomato Yellow Leaf Curl Virus',
  'Tomato ➔ Tomato mosaic virus',
  'Tomato ➔ healthy'
]


def home_view(request):
    prediction = None
    certainty = None

    if request.method == 'POST' and request.FILES.get('img'):
        img_file = request.FILES['img']
        img = Image.open(img_file).resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        result = model.predict(img_array)
        pred_index = np.argmax(result)
        prediction = class_names[pred_index]
        certainty =  round(float(result[0][pred_index]) * 100, 2) 

    return render(request, 'mlapp/home.html', {'result': prediction, 'accuracy': certainty})

# About Us page
def about_us_view(request):
    return render(request, 'mlapp/about_us.html')

# About Project page
def about_project_view(request):
    return render(request, 'mlapp/about_project.html')