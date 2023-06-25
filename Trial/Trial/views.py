from django.http import HttpResponse
from django.shortcuts import render, redirect
from PIL import Image
import numpy as np
from django.conf import settings
import torch
import os

def home(request):
    return render(request, "home.html")

def redirect_view(request):
    return render(request, "home.html")


def drowsy(request):
    # Get the path to the script you want to execute
    script_path = 'C:/Users/Acer/FinalYearProject/cv.py'
    
    # Execute the script
    os.system(f'py {script_path}')

    return redirect('/success/')

def detect(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        image = Image.open(image_file)

        model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Acer/FinalYearProject/yolov5/runs/train/exp/weights/last.pt', force_reload = True)
        det = model(image) #loading the image into the model for detections
        np_array = np.squeeze(det.render())
        img = Image.fromarray(np.uint8(np_array))
        img.save('media/detection.png')

        return render(request, 'detection.html', {'result' : img})