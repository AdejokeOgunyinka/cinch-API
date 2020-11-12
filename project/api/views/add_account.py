from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from api.lib.response import Response
from payment.bank_verification import BankVerify
from payment.add_account import AddAccount


class AccountVerifyViewSet(ViewSet):
    @action(methods=['post'], detail=False, permission_classes=[IsAuthenticated], url_path='*')
    def save_account_details(self, request):

        account_details = BankVerify.call(data=request.data)

        # If account is invalid
        if account_details.failed:
            return Response(errors=account_details.error.value, status=status.HTTP_400_BAD_REQUEST)

        res = account_details.value
        status_message = res.get('status')

        if status_message:
            user_data = res.get('data')

            account_number, account_name = user_data.get('account_number'), user_data.get('account_name')
            bank_name, bank_code = request.data.get('bank_name'), request.data.get('bank_code')

            user_id = request.user.id

            save_data = AddAccount.call(account_name=account_name, account_number=account_number,
                                        bank_name=bank_name, bank_code=bank_code, user_id=user_id)

            # If Artist_id already exists with a register account and saving fails
            if save_data.failed:
                return Response(errors=save_data.error.value, status=status.HTTP_400_BAD_REQUEST)

            # If all checks are successful and data is saved
            return Response(data=save_data.value, status=status.HTTP_201_CREATED)
