from django.urls import path
from . import views
app_name="api"

urlpatterns = [
    path("create-user/",views.UserListView.as_view(),name="create-user"),
    path("user-detail/<int:pk>/",views.UserDetailListView.as_view(),name="user-detail"),
    path("add-expenses/",views.ExpensesView.as_view(),name="add-expenses"),
    path('individual-expenses/<int:pk>',views.IndividualExpensesView.as_view(),name="individual-expenses"),
    path("overall-expenses/",views.OverallExpensesView.as_view(),name="overall-expenses"),
    path("balance-sheet/",views.BalanceSheetView.as_view(),name="balance-sheet"),
    path("balance-sheet/<int:pk>/",views.BalanceSheetDetailVIew.as_view(),name="balance-sheet-detail")

]