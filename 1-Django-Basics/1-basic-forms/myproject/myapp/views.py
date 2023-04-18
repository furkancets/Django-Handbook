from django.shortcuts import render
from myapp.forms import BookingForm
from django.http import HttpResponse

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('Form successfully submitted') 
    context = {"form" : form}
    return render(request, "booking.html", context)