from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PlantRegistry
from .serializers import PlantRegistrySerializer
from rest_framework.permissions import AllowAny

# Create your views here.

#CREATE 

class CreateResitryPlantView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = PlantRegistrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response({'message':'Creado'} , status=status.HTTP_201_CREATED)
    
#READ ALL

class RetrievePlantsView(APIView):
    permission_classes=(AllowAny,)

    def get(self, request):
        plants_list=PlantRegistry.objects.all()
        serializer=PlantRegistrySerializer(plants_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#RAED ONE
class RetrievePlantsidView(APIView):
    permission_classes=(AllowAny,)

    def get(self, request, pk):
        plants_list=get_object_or_404(PlantRegistry, pk=pk)
        serializer=PlantRegistrySerializer(plants_list)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateRegitryPlant(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        plants_list=get_object_or_404(PlantRegistry, pk=pk)
        serializer=PlantRegistrySerializer(plants_list)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        plants = PlantRegistry.objects.get(pk=pk)
        serializer = PlantRegistrySerializer(plants, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DELETE VIEW PK
class DeletePlantRegistryView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk):
       plants_list=get_object_or_404(PlantRegistry, pk=pk)
       serializer=PlantRegistrySerializer(plants_list)
       return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        plant = get_object_or_404(PlantRegistry, pk=pk)
        #plant = self.get_object(pk)
        plant.status = False
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteallPlantRegistryView(APIView):

    def get(self, request):
        plants_list=PlantRegistry.objects.all()
        serializer=PlantRegistrySerializer(plants_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        plant = PlantRegistry.objects.all()
        plant.status = False
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        