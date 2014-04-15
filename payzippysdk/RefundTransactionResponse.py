from payzippysdk import Constants


class RefundTransactionResponse(object):
    def __init__(self, params):
        self.params = params

    def get_transaction_response_params(self):
        return self.params

    def get_merchant_transaction_id(self):
        return self.params.get(Constants.MERCHANT_TRANSACTION_ID)

    def get_payzippy_transaction_id(self):
        return self.params.get(Constants.PAYZIPPY_TRANSACTION_ID)

    def get_refund_amount(self):
        return self.params.get(Constants.REFUND_AMOUNT)

    def get_refund_status(self):
        return self.params.get(Constants.REFUND_STATUS)

    def get_refund_response_code(self):
        return self.params.get(Constants.REFUND_RESPONSE_CODE)

    def get_refund_response_message(self):
        return self.params.get(Constants.REFUND_RESPONSE_MESSAGE)

    def get_bank_arn(self):
        return self.params.get(Constants.BANK_ARN)

    def get_transaction_time(self):
        return self.params.get(Constants.TRANSACTION_TIME)

    def get_currency(self):
        return self.params.get(Constants.CURRENCY)

    def get_udf1(self):
        return self.params.get(Constants.UDF1)

    def get_udf2(self):
        return self.params.get(Constants.UDF2)

    def get_udf3(self):
        return self.params.get(Constants.UDF3)

    def get_udf4(self):
        return self.params.get(Constants.UDF4)

    def get_udf5(self):
        return self.params.get(Constants.UDF5)