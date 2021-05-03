from .models import Category
def cats_renderer(request):
    return {
       'all_cats': Category.objects.all(),
    }