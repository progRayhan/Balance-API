from taka.models import Balances, Bank
from rest_framework.views import APIView
from taka.api.serializers import BalancesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class balance_list(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        balances = Balances.objects.all()
        serializer = BalancesSerializer(balances, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BalancesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
class balance_detail(APIView):
    def get(self, request, pk):
        try:
            balances = Balances.objects.get(pk=pk)
        except Balances.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = BalancesSerializer(balances)
        return Response(serializer.data)
    
    def put(self, request, pk):
        balances = Balances.objects.get(pk=pk)
        serializer = BalancesSerializer(balances, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        balances = Balances.objects.get(pk=pk)
        balances.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class BalanceCreate(generics.CreateAPIView):
#     serializer_class = BalancesSerializer
#     # permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Balances.objects.all()
    
#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         balances = Balances.objects.get(pk=pk)
#         # my method goes here
#         account_holder = self.request.user
#         review_queryset = Balances.objects.filter(banklist=balances, account_holder=account_holder)
        
#         if review_queryset.exists():
#             raise ValidationError("Error!")
        
#         serializer.save(banklist=balances, account_holder=account_holder)

# class BalanceList(generics.ListAPIView):
#     serializer_class = BalancesSerializer
    
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Balances.objects.filter(watbanklistchlist=pk)
    
    
# class BalanceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Balances.objects.all()
#     serializer_class = BalancesSerializer