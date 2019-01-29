from django.shortcuts import render

# Create your views here.
def tran_comp(request):
    template_name = "transaction/tran_comp.html"
    context_data = {}
    return render(request,template_name,context_data)


def tran_fail(request):
    template_name = "transaction/tran_fail.html"
    context_data = {}
    return render(request,template_name,context_data)
