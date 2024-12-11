from graphene_django import DjangoObjectType
import graphene
from .models import Bank, Branch

class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = ("id", "name", "branches")

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch
        fields = ("ifsc", "bank", "branch", "address", "city", "district", "state")

class Query(graphene.ObjectType):
    branches = graphene.List(BranchType)

    def resolve_branches(root, info):
        return Branch.objects.select_related("bank").all()

schema = graphene.Schema(query=Query)
