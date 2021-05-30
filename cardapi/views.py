import requests
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CardSerializer

from .models import Card


class CardAPIView(APIView):
    def get_object(self,id):
        try:
            return Card.objects.get(number=id)
        except:
            return None

    def getTheAPIData(self, id):

        url = "https://lookup.binlist.net/"
        url += id
        print(url)
        response = requests.request("GET", url)
        js_data = json.loads(response.text)
        d = {}
        d['scheme'] = js_data['scheme']
        d['type'] = js_data['type']
        d['brand'] = js_data['brand']
        d['prepaid'] = bool(js_data.get('prepaid',False))
        d['country'] = js_data['country']['name']
        d['number'] = str(id)
        d['name'] = js_data['bank']['name']
        d['url'] = js_data['bank']['url']
        d['phone'] = js_data['bank']['phone'].replace(' ','')
        d['city'] = js_data['bank'].get('city',None)

        return d

    def get(self, request, id):
        data = self.get_object(id)
        if(not data):
            data = self.getTheAPIData(id)
        serial = CardSerializer(data=data)
        if(serial.is_valid()):
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response(serial.errors, status=status.HTTP_404_NOT_FOUND)

