from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tickets.models import Tickets
from tickets.serializers import TicketsSerializer


@csrf_exempt #allows to make POST requests without a CSRF token
def tickets_list(request) :

    if request.method == 'GET' :
        tickets = Tickets.objects.all()
        serializer = TicketsSerializer(tickets,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST' :
        data = JSONParser().parse(request)
        serializer = TicketsSerializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def add_single_ticket(request) :

    if request.method == 'POST' :
        data = JSONParser().parse(request)
        serializer = TicketsSerializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data,status=201)

    return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def last_ticket(request) :

    if request.method == 'GET' :

        last_ticket = Tickets.objects.latest('id') #0 tickets case not considered
        serializer = TicketsSerializer(last_ticket)
        return JsonResponse(serializer.data)

#missing update ticket based on ID
@csrf_exempt
def classify_ticket(request,pk) :

    try :
        ticket = Tickets.objects.get(pk=pk)
    except Tickets.DoesNotExist :
        return HttpResponse(status=404) 

    if request.method == 'PUT' :
        data = JSONParser().parse(request)
        serializer = TicketsSerializer(ticket,data=data)
        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

        