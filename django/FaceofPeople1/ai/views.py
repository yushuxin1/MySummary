from django.http import HttpResponse
from django.shortcuts import render
import random
import json
import requests

# Create your views here.
def ai(request):
    with open("./json1.txt", "r") as f:
        json1 = json.load(f)
        f.close()
    image_file = "./static/" + str(random.random() * 10) + ".jpg"
    image_i = image_file[1:]
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        image = request.FILES.get("photo")
        if not image:
            imageUrl = request.POST.get('photoURL')
            # print(imageUrl)
            response = requests.get(imageUrl)
            image = response.content
            with open(image_file, "wb") as f:
                f.write(image)
                f.close()
        else:
            with open(image_file, "wb") as f:
                f.write(image.read())
                f.close()
                print(image_i)
        return render(request, "index.html", context={"i": image_i, "t": json1})
