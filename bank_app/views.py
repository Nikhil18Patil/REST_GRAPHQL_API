from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankListAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all banks",
        operation_description="Retrieve a list of all banks.",
        responses={
            200: openapi.Response(
                description="List of banks returned successfully",
                examples={
                    "application/json": {
                        "banks": [
                            {"id": 1, "name": "Bank of India"},
                            {"id": 2, "name": "State Bank of India"}
                        ]
                    }
                },
            ),
            500: openapi.Response(
                description="Internal server error",
                examples={
                    "application/json": {"error": "An error occurred: Details of the error."}
                },
            ),
        },
    )
    def get(self, request):
        """
        Retrieve a list of all banks available in the database.
        """
        try:
            # import pdb ; pdb.set_trace()
            banks = Bank.objects.all()
            serializer = BankSerializer(banks, many=True)
            return Response({"banks": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class BranchDetailsAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Get branch details by IFSC code",
        operation_description="Retrieve details of a specific branch using its IFSC code.",
        manual_parameters=[
            openapi.Parameter(
                "branch_ifsc",
                openapi.IN_PATH,
                description="IFSC code of the branch",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                description="Branch details returned successfully",
                examples={
                    "application/json": {
                        "branch": {
                            "ifsc": "SBIN0000001",
                            "bank": {"id": 1, "name": "State Bank of India"},
                            "branch": "Main Branch",
                            "address": "123 Street, City",
                            "city": "Mumbai",
                            "district": "Mumbai",
                            "state": "Maharashtra"
                        }
                    }
                },
            ),
            404: openapi.Response(
                description="Branch not found",
                examples={"application/json": {"error": "Branch not found"}},
            ),
            500: openapi.Response(
                description="Internal server error",
                examples={
                    "application/json": {"error": "An error occurred: Details of the error."}
                },
            ),
        },
    )
    def get(self, request, branch_ifsc):
        """
        Retrieve details of a specific branch using its IFSC code.
        """
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

