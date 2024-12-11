from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer


class BankListAPIView(APIView):
    def get(self, request):
        try:
            banks = Bank.objects.all()
            serializer = BankSerializer(banks, many=True)
            return Response({"banks": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class BranchDetailsAPIView(APIView):
    def get(self, request, branch_ifsc):
        try:
            branch = Branch.objects.select_related("bank").get(ifsc=branch_ifsc)
            serializer = BranchSerializer(branch)
            return Response({"branch": serializer.data}, status=status.HTTP_200_OK)
        except Branch.DoesNotExist:
            return Response(
                {"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
