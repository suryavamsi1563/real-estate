from django.shortcuts import render
from .forms import testform
# Create your views here.
def tran_comp(request):
    template_name = "transaction/tran_comp.html"
    context_data = {}
    return render(request,template_name,context_data)


def tran_fail(request):
    template_name = "transaction/tran_fail.html"
    context_data = {}
    return render(request,template_name,context_data)


def test_view(request):
    template_name = "transaction/test.html"
    test_form = testform()
    
    if request.POST:
        test_form = testform(request.POST)
        if test_form.is_valid():
            print("good")

    context_data = {'form':testform}
    return render(request,template_name,context_data)