from .models import Category

def global_categories(request):
    links=Category.objects.all()
    return dict(links=links)
    