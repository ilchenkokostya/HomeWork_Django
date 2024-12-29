from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'second_task/index.html')

def fn_template(request):
    return render(request, 'second_task/func_template.html')

class cls_template(TemplateView):
    template_name = 'second_task/class_template.html'