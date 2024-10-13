from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
# Create your views here.

@api_view(["GET"])

def mywish(request):
    return Response("Hello gdmrng")

@api_view(["GET"])

def fresh(request,age):
    return Response(f"MY AGE IS:{age}")

@api_view(["POST"])

def fresh(request):
    age = request.data.get("age")

    if age is None:
        return Response({"error": "Age is required"}, status=400)
    
    person = Person(age=age)
    person.save()

    return Response({"message": f"MY AGE IS: {person.age}"})
    

