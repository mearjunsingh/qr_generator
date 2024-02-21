from django.shortcuts import render

from app.data.qr_data_e5_live_test_event_1_first_5000_tickets import QR_DATA
from app.data.pharma_expo_stall_diff_label_qrs import DIFF_LABELED_QR_DATA
from app.data.pharma_expo_stall_same_label_qrs import SAME_LABELED_QR_DATA


def index(request):
    return render(request, "index.html")


def qr(request):
    return render(request, "qr.html", {"qrs": QR_DATA})


def same_labeled_qr(request):
    return render(
        request,
        "same_labeled_qr.html",
        {
            "qrs": SAME_LABELED_QR_DATA,
        },
    )


def diff_labeled_qr(request):
    return render(
        request,
        "diff_labeled_qr.html",
        {
            "qrs": DIFF_LABELED_QR_DATA,
        },
    )
