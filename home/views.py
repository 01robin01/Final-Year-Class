
from django.shortcuts import redirect, render
from .models import Category, Item, ItemImage
from PIL import Image
from django.contrib import messages
import imagehash

def index(request):
    items = (
        Item.objects
        .prefetch_related('images')
        .order_by('-id')[:10]
    )

    context = {
        "items": items
    }

    return render(request, "Index.html", context)

def search(request):
    if request.method == 'POST':
        query = request.POST.get("q", "")
        img = request.FILES.get("img", None)
        
        results = Item.objects.none()

        if query:
            results = Item.objects.filter(title__icontains=query, is_deleted=False)
            print("Text Results:", results)

        if img is not None:
            print("Image uploaded for search.")
            image = Image.open(img)
            phash = imagehash.phash(image)
            similar_images = ItemImage.objects.filter(perceptual_hash__startswith=str(phash)[:4]).select_related('item')
            image_item_ids = [img_obj.item.id for img_obj in similar_images]
            image_results = Item.objects.filter(id__in=image_item_ids, is_deleted=False)
            results = results | image_results
            print("Image Results:", image_results)

        context = {
            "query": query,
            "matches": results.distinct(),
            "categories": Category.objects.all(),
            "img_searched": img is not None
        }

        return render(request, "search-page.html", context, status=201)



def item_details(req,id):
    context = {
        'item':Item.objects.get(id=id),
        'related_items': Item.objects.filter(category=Item.objects.get(id=id).category).exclude(id=id)[:5]
    }
    return render(req,'item-details.html',context)


def dashboard(request):
    lost_items = Item.objects.filter(item_type='lost', is_deleted=False)
    found_items = Item.objects.filter(item_type='found', is_deleted=False)
    context = {
        'lost_items': lost_items,
        'found_items': found_items
    }
    return render(request, 'dashboard.html',context)