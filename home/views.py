from django.shortcuts import render, HttpResponse,get_list_or_404
from datetime import datetime
from home.models import Contact
from django.contrib import messages


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact
from .serializers import contactSerializer


class contactlist(APIView):
    def get(self,request):
        contact1=Contact.objects.all()
        serializer=contactSerializer(contact1,many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 