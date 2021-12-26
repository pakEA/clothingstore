from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from adminapp.forms import AdminShopUserUpdateForm, AdminProductCategoryCreateForm, AdminProductUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    page_title_key = 'page_title'
    page_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.page_title_key] = self.page_title
        return context


class ShopUserListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/index.html'
    page_title = 'admin/users'


class ShopUserAdminUpdate(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = get_user_model()
    form_class = AdminShopUserUpdateForm
    success_url = reverse_lazy('new_admin:index')
    pk_url_kwarg = 'user_pk'
    page_title = 'admin/users/edit'


class ShopUserAdminDelete(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('new_admin:index')
    pk_url_kwarg = 'user_pk'
    page_title = 'admin/users/delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductCategoryList(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = ProductCategory
    page_title = 'admin/categories'


class ProductCategoryCreate(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    form_class = AdminProductCategoryCreateForm
    success_url = reverse_lazy('new_admin:categories')
    page_title = 'admin/category/create'


class ProductCategoryUpdate(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = ProductCategory
    form_class = AdminProductCategoryCreateForm
    success_url = reverse_lazy('new_admin:categories')
    page_title = 'admin/category/update'


class ProductCategoryDelete(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('new_admin:categories')
    page_title = 'admin/category/delete'


@user_passes_test(lambda user: user.is_superuser)
def category_products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    object_list = category.product_set.all()
    context = {
        'page_title': f'category {category.name}/products',
        'category': category,
        'object_list': object_list,
    }
    return render(request, 'mainapp/category_products_list.html', context)


@user_passes_test(lambda user: user.is_superuser)
def category_product_create(request, category_pk):
    category = get_object_or_404(ProductCategory, pk=category_pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('new_admin:category_products',
                                                kwargs={'pk': category_pk}))
    else:
        form = AdminProductUpdateForm(initial={'category': category})

    context = {
        'page_title': 'product/create',
        'category': category,
        'form': form,
    }
    return render(request, 'mainapp/product_update.html', context)


class ProductDetail(SuperUserOnlyMixin, PageTitleMixin, DetailView):
    model = Product
    page_title = 'admin/products'
