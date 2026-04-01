from django.shortcuts import  redirect, render
from .models import Category, Item, ItemImage
from PIL import Image
import imagehash

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


def search(request):
    if request.method == 'POST':
        query = request.POST.get("q", "")
        img = request.FILES.get("img", None)
        if query:
            results = Item.objects.filter(title__icontains=query)
            print("Text Results:", results)

        if img is not None:
            print("Image uploaded for search.")
            image = Image.open(img)
            phash = imagehash.phash(image)
            similar_images = ItemImage.objects.filter(perceptual_hash__startswith=str(phash)[:4]).select_related('item')
            image_item_ids = [img.item.id for img in similar_images] # type: ignore
            image_results = Item.objects.filter(id__in=image_item_ids, is_deleted=False)
            results = results | image_results # type: ignore
            print("Image Results:", image_results)



        context = {
            "query": query,
            "matches": results
        }

        return render(request, "search-page.html", context,status=201)
    
    def item_details(req,id):
        context = {
        'item':Item.objects.get(id=id),
        'related_items': Item.objects.filter(category=Item.objects.get(id=id).category).exclude(id=id)[:5]
    }
        return render(req,'item-details.html',context)


