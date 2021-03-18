from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views import View
from .models import Client as Client
# Create your views here.

class ClientAdd(View):

    def get(self, request):
        return render(request, 'add_client.html')

    def post(self, request):
        short_name = request.POST.get('short_name')
        full_name = request.POST.get('full_name')
        city = request.POST.get('city')
        street = request.POST.get('street')
        tax_number = request.POST.get('tax_number')
        industry = request.POST.get('industry')
        website = request.POST.get('website')
        source_lead = request.POST.get('source_lead')
        status = request.POST.get('status')

        Client.objects.create(short_name=short_name,
                             full_name=full_name,
                             city=city,
                             street=street,
                             tax_number=tax_number,
                             industry=industry,
                             website=website,
                             source_lead=source_lead,
                             status=status)

        context = {'message':'Dodano do bazy'}

        return render(request, "list_client_code.html", context)

class ClientList(View):

    def get(self, request):
        client_list = Client.objects.all()
        print(client_list)
        return render(request, 'list_client.html', context={'client_list': client_list})

