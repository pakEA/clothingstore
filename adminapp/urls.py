from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.ShopUserListView.as_view(), name='index'),
    path('user/update/<int:user_pk>/', adminapp.ShopUserAdminUpdate.as_view(),
         name='user_update'),
    path('user/delete/<int:user_pk>/', adminapp.ShopUserAdminDelete.as_view(),
         name='user_delete'),

    path('categories/', adminapp.ProductCategoryList.as_view(), name='categories'),
    path('category/create/', adminapp.ProductCategoryCreate.as_view(),
         name='category_create'),
    path('category/update/<int:pk>/', adminapp.ProductCategoryUpdate.as_view(),
         name='category_update'),
    path('category/delete/<int:pk>/', adminapp.ProductCategoryDelete.as_view(),
         name='category_delete'),
    path('category/<int:pk>/products/', adminapp.category_products,
         name='category_products'),
    path('category/<int:category_pk>/product/create/', adminapp.category_product_create,
         name='category_product_create'),

    path('product/<int:pk>/', adminapp.ProductDetail.as_view(), name='product_view'),
]
