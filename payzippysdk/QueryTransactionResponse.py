from payzippysdk import Constants


class QueryTransactionResponse(object):

    def __init__(self, params):
        self.params = params

    def get_transaction_response_params(self):
        return self.params

    def get_transaction_status(self):
        return self.params.get(Constants.TRANSACTION_STATUS)

    def get_transaction_response_code(self):
        return self.params.get(Constants.TRANSACTION_RESPONSE_CODE)

    def get_fraud_action(self):
        return self.params.get(Constants.FRAUD_ACTION)

    def get_fraud_details(self):
        return self.params.get(Constants.FRAUD_DETAILS)

    def get_transaction_amount(self):
        return self.params.get(Constants.TRANSACTION_AMOUNT)

    def get_merchant_transaction_id(self):
        return self.params.get(Constants.MERCHANT_TRANSACTION_ID)

    def get_payzippy_transaction_id(self):
        return self.params.get(Constants.PAYZIPPY_TRANSACTION_ID)

    def get_bank_arn(self):
        return self.params.get(Constants.BANK_ARN)

    def get_payment_method(self):
        return self.params.get(Constants.PAYMENT_METHOD)

    def get_transaction_time(self):
        return self.params.get(Constants.TRANSACTION_TIME)

    def get_transaction_currency(self):
        return self.params.get(Constants.TRANSACTION_CURRENCY)

    def get_transaction_type(self):
        return self.params.get(Constants.TRANSACTION_TYPE)

    def get_emi_months(self):
        return self.params.get(Constants.EMI_MONTHS)

    def get_transaction_response_message(self):
        return self.params.get(Constants.TRANSACTION_RESPONSE_MESSAGE)
