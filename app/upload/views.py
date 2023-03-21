from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .models import Upload


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        image_type = request.POST['image_type']

        if settings.USE_S3:
            upload = Upload(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
            print(image_url)
        return render(request, "upload/upload.html", {
            "image_url": image_url,
            "image_type": image_type,
        })
    return render(request, "upload/upload.html")
