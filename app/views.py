from django.shortcuts import render

# from app.data import NADA_12000_DATA, LABELED_QR_DATA, NADE_2000_DATA


NADE_2000_DATA = [
    "https://www.seiu1000.org/sites/main/files/imagecache/hero/main-images/camera_lense_0.jpeg"
    for _ in range(2000)
]


def index(request):
    return render(request, "index.html")


def qr(request):
    return render(request, "qr.html", {"qrs": NADE_2000_DATA})


# def labeled_qr(request):
#     return render(request, "labeled_qr.html", {"qrs": LABELED_QR_DATA})
