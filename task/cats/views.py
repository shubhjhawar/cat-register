from django.shortcuts import render
# Create your views here.

from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from .utils import *
from .messages import *
import logging
logger = logging.getLogger('django')

# used to add a new cat in the database along with it all the details
class AddCatView(GenericAPIView):
    serializer_class =CatDetailSerializer

    def post(self, request):
        try:
            serializer =CatDetailSerializer(data=request.data)
            # if the provided data is valid, it gets stored into the database
            if serializer.is_valid():
                serializer.save()
                logger.info("cat registered successfully")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.info("error while registering a cat")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            logger.info(failure_msg)
            return Response({"Failure":failure_msg}, status=status.HTTP_400_BAD_REQUEST)

class AllCatView(viewsets.ModelViewSet):
    serializer_class = CatDetailSerializer
    queryset = CatDetailModel.objects.all()

    # this is used to get a list of all the cats present in our database
    @action(detail=False, methods=['GET'], url_path="")
    def all_cats(self, request):
        try:
            # declare the serializer, get all the objects from the database and pass it through the serializer
            serializer = CatDetailSerializer
            queryset = CatDetailModel.objects.all()
            all_cats = serializer(queryset, many=True)
            logger.info("list of cats was displayed successfully")
            return Response(all_cats.data, status=status.HTTP_200_OK)
        except Exception:
            logger.info(failure_msg)
            return Response({"Failure":failure_msg}, status=status.HTTP_400_BAD_REQUEST)

    # used to edit a cat's details, it takes the cat_id from the url
    @action(detail=False, methods=['PUT'], url_path="edit/(?P<cat_id>\d+)")
    def edit_cat(self, request, cat_id):
        try:
            data= request.data

            # provided data gets updated for the selected cat
            update_cat_details(data, cat_id)            #this function is found in 'utils.py'
            logger.info(update_msg)
            return Response({"Success":update_msg}, status=status.HTTP_200_OK)
        except Exception:
            logger.info(failure_msg)
            return Response({"Failure":failure_msg}, status=status.HTTP_400_BAD_REQUEST)

    # used to remove a cat from the database, it's id is provided in the url
    @action(detail=False, methods=['GET'], url_path="remove/(?P<cat_id>\d+)")
    def remove_cat(self, request, cat_id):
        try:
            cat_object = CatDetailModel.objects.get(id=cat_id).delete()             #we get the required object from the database and delete it
            logger.info(remove_msg)
            return Response({"Success":remove_msg}, status=status.HTTP_200_OK)
        except Exception:
            logger.info(failure_msg)
            return Response({"Failure":failure_msg}, status=status.HTTP_400_BAD_REQUEST)
