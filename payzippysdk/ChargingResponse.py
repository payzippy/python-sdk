import Constants
from HashUtil import HashUtil
from payzippysdk import Config


class ChargingResponse(object):
    """
    ChargingResponse is built from the parameters received in charging callback URL.
    """

    def __init__(self, response_param):
        self.params = {}
        response_param = dict(response_param)
        for key in response_param:
            if key in Config.blacklist_params:
                continue
            if type(response_param[key]) is list:
                self.params[key] = response_param[key][0]
            else:
                self.params[key] = response_param[key]

    def get_response_params(self):
        return self.params

    def is_valid_response(self):
        hash_util = HashUtil(self.params, self.params.get(Constants.HASH_METHOD))
        return self.params.get(Constants.HASH) == hash_util.generate_hash()

    def is_fraud(self):
        return Constants.ACCEPT == self.params.get(Constants.FRAUD_ACTION).upper()

    def is_transaction_successful(self):
        return Constants.SUCCESS == self.params.get(Constants.TRANSACTION_STATUS).upper()

    def get_payzippy_transaction_id(self):
        return self.params.get(Constants.PAYZIPPY_TRANSACTION_ID)

    def get_merchant_transaction_id(self):
        return self.params.get(Constants.MERCHANT_TRANSACTION_ID)

    def get_transaction_status(self):
        return self.params.get(Constants.TRANSACTION_STATUS)

    def get_transaction_response_message(self):
        return self.params.get(Constants.TRANSACTION_RESPONSE_MESSAGE)

    def get_transaction_response_code(self):
        return self.params.get(Constants.TRANSACTION_RESPONSE_CODE)

    def get_fraud_action(self):
        return self.params.get(Constants.FRAUD_ACTION)

    def get_fraud_details(self):
        return self.params.get(Constants.FRAUD_DETAILS)

    def get_transaction_amount(self):
        return self.params.get(Constants.TRANSACTION_AMOUNT)

    def get_payment_method(self):
        return self.params.get(Constants.PAYMENT_METHOD)

    def get_bank_name(self):
        return self.params.get(Constants.BANK_NAME)

    def get_emi_months(self):
        return self.params.get(Constants.EMI_MONTHS)

    def get_transaction_currency(self):
        return self.params.get(Constants.TRANSACTION_CURRENCY)

    def get_transaction_time(self):
        return self.params.get(Constants.TRANSACTION_TIME)

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

    def get_hash_method(self):
        return self.params.get(Constants.HASH_METHOD)

    def get_hash(self):
        return self.params.get(Constants.HASH)

    def get_merchant_id(self):
        return self.params.get(Constants.MERCHANT_ID)

    def get_merchant_key_id(self):
        return self.params.get(Constants.MERCHANT_KEY_ID)

    def is_international(self):
        return self.params.get(Constants.IS_INTERNATIONAL).lower() == "true"

    def get_version(self):
        return self.params.get(Constants.VERSION)
