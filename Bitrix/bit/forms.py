from django import forms
from .models import *


######### task form #############
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

######### end task form ############

######### register form #############

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"

######### end register form #############


######### Invoice Form ########

class InvoiceModelForm(forms.ModelForm):
    class Meta:
        model = MakeInvoiceModel
        fields = '__all__'

####### end Invoice Form  #######