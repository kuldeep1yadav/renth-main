from django.shortcuts import render

# Create your views here.
def dashboard_home(request):
    return render(request, 'home.html')

def property(request):
    return render(request, 'property-grid.html')

def propertysingle(request):
    return render(request, 'property-single.html')

def blog(request):
    return render(request, 'blog-grid.html')

def singleblog(request):
    return render(request, 'blog-single.html')

def hotelowner(request):
    return render(request, 'hotelowner.html')

def about(request):
    return render(request, 'about.html')    