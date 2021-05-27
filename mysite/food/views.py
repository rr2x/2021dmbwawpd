from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# region
# function based view
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'food/index.html', context)
# endregion


class IndexClassView(ListView):  # class based view
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def anotherlink(request):
    return HttpResponse('Hello Again')


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

# region
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)
# endregion


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    # if no context_object_name, the default value is 'object'

# region
# def create_item(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')

#     return render(request, 'food/item-form.html', {'form': form})
# endregion


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        # associate currently logged in user to this item
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item})
