from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('task', views.task),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('register', views.register),
    path('register/registeration_successful', views.fillRegisteration),
    path('login', views.login),
    path('calender/', views.calender),
    path('invoice/', views.invoice),
    path('Invoice/showInvoice', views.fillInvoice, name='Invoice/showInvoice'),
    path('showInvoice', views.showinvoice),
    path('editInvoice/<int:id>', views.editinvoice),
    path('updateInvoice/<int:id>', views.updateinvoice),
    path('deleteInvoice/<int:id>', views.destroyinvoice),
    path('ViewInvoice/<int:id>', views.viewinvoice),
    #path('division/<int:id>', views.division),
    #path('addition/<int:id>', views.addition),

]
