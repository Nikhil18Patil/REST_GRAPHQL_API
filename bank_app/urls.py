from django.urls import path
from graphene_django.views import GraphQLView
from .views import BankListAPIView, BranchDetailsAPIView
from .schema import schema

urlpatterns = [
    path("api/banks/", BankListAPIView.as_view(), name="bank_list"),
    path("api/branches/<str:branch_ifsc>/", BranchDetailsAPIView.as_view(), name="branch_details"),
    path("gql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
