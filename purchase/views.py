from purchase.models import Purchase
from purchase.serializers import Purchaseserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PurchaseList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        purchase = request.meta['HTTP_COMPANY']
        purchase = Purchase.objects.all(purchase=purchase)
        serializer = Purchaseserializers(purchase, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Purchaseserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Purchase.objects.get(id=id)
        except Purchase.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Purchase = self.get_object(id)
        serializer = Purchaseserializers(Purchase)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Purchase = self.get_object(id)
        serializer = Purchaseserializers(Purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Purchase = self.get_object(id)
        Purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
