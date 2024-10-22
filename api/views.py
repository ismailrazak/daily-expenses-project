from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import UserSerializer,ExpenseSerializer,OwnedBySerializer
from django.contrib.auth import get_user_model
from .models import Expense ,OwnedBy
from rest_pandas import PandasExcelRenderer,PandasView
# Create your views here.

# allows to download all the total expenses.
class BalanceSheetView(PandasView):
    renderer_classes = [PandasExcelRenderer]
    serializer_class = OwnedBySerializer
    queryset = OwnedBy.objects.all()

#allows download of individual expenses.
class BalanceSheetDetailVIew(PandasView):
    renderer_classes = [PandasExcelRenderer]
    serializer_class = OwnedBySerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_user_model().objects.get(id=pk)
        return user.owes_to.all()


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class UserDetailListView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

#for add expenses url.
class ExpensesView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    #sql optimziation by using prefetch_related
    queryset = Expense.objects.prefetch_related("owned_by__username")

class IndividualExpensesView(ListAPIView):
    serializer_class =OwnedBySerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        user=get_user_model().objects.get(id=pk)
        # sql optimziation by using prefetch_related
        return user.owes_to.prefetch_related("expense").all()

class OverallExpensesView(ListAPIView):
    serializer_class = OwnedBySerializer
    # sql optimziation by using select_related
    queryset = OwnedBy.objects.select_related("expense","username").all()

