from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('export/', views.export, name='export'),
    path('export_excel', views.export_excel, name='export_excel'),
    path('export_pandas_df', views.export_pandas_dataframe, name='export_pandas_df')
]
