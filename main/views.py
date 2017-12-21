from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from main.models import Pet
from main.serializers import PetSerializer


@csrf_exempt
def cat_list(request, user=None, pk=None):
    if request.method == 'GET':
        if pk:
            cats = Pet.objects.filter(type='1', id=pk, owner=User.objects.get(username=user))
        else:
            cats = Pet.objects.filter(type='1', owner=User.objects.get(username=user))
        serializer = PetSerializer(cats, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if pk:
            cat = Pet.objects.get(id=pk)
            serializer = PetSerializer(cat, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        else:
            serializer = PetSerializer(data=data)
            if serializer.is_valid():
                serializer.save(owner=User.objects.get(username=user), type='1')
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if pk:
            try:
                cat = Pet.objects.get(type='1', id=pk)
                cat.delete()
                return HttpResponse('{"success": "Pet has been deleted"}', status=201)
            except Pet.DoesNotExist:
                return HttpResponse('{"error": "Pet does not exist"}', status=400)
        else:
            return HttpResponse('{"error": "Please specify the pet id"}', status=400)


@csrf_exempt
def dog_list(request, user=None, pk=None):
    if request.method == 'GET':
        if pk:
            dogs = Pet.objects.filter(type='2', id=pk, owner=User.objects.get(username=user))
        else:
            dogs = Pet.objects.filter(type='2', owner=User.objects.get(username=user))
        serializer = PetSerializer(dogs, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST' or request.method == 'PUT':
        data = JSONParser().parse(request)

        if pk:
            dog = Pet.objects.filter(type='2', id=pk)
            serializer = PetSerializer(dog, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        else:
            serializer = PetSerializer(data=data)
            if serializer.is_valid():
                serializer.save(owner=User.objects.get(username=user), type='2')
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if pk:
            try:
                dog = Pet.objects.get(type='2', id=pk)
                dog.delete()
                return HttpResponse('{"success": "Pet has been deleted"}', status=201)
            except Pet.DoesNotExist:
                return HttpResponse('{"error": "Pet does not exist"}', status=400)
        else:
            return HttpResponse('{"error": "Please specify the pet id"}', status=400)
