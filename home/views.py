from django.shortcuts import render
from .models import Item,ItemImage

def index(request):
    
    items = (
        Item.objects
        .prefetch_related('images')
        .order_by('-id')[:10]
    )

  
    if not items:
        items = [
            {
                "title": "Lost Wallet",
                "location": "Kathmandu",
                "status": "Lost",
                "images": []
            },
            {
                "title": "Found Phone",
                "location": "Lalitpur",
                "status": "Found",
                "images": []
            }
        ]

    context = {
        "items": items
    }


    return render(request, "Index.html", context)


