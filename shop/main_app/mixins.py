from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View

from .models import Category, Cart, Customer, Notebook, Smartphone


class CategoryDetailMixin(SingleObjectMixin):

    CATEGORY_SLUG2PRODUCT_MODEL = {
        'notebooks': Notebook,
        'smartphones': Smartphone
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()
        return context
