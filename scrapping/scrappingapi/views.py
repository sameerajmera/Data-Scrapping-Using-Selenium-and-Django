from django.shortcuts import render
from rest_framework.response import Response
from .scrap import scrapFunct
from django.http import HttpResponse
from rest_framework.views import APIView 
import pandas as pd
import json
# Create your views here.

class scrapAPI(APIView):
    def get(self,request):
        results = scrapFunct()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=filename.csv'
        results.to_csv(path_or_buf=response,sep=',',float_format='%.2f',index=False,decimal=".")
        return (response)