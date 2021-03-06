try:
    import json
except ImportError:
    import simplejson as json

import Constants
from HashUtil import HashUtil
from payzippysdk.QueryTransactionResponse import QueryTransactionResponse


class QueryResponse(object):

    def __init__(self, params):
        self.response_params = {}
        self.transaction_responses = []
        self.response_params = json.loads(params)
        for transaction_response in self.response_params[Constants.DATA]:
            self.transaction_responses.append(QueryTransactionResponse(transaction_response))

    def get_response_params(self):
        return self.response_params

    def get_transaction_responses(self):
        return self.transaction_responses

    def get_status_code(self):
        return self.response_params.get(Constants.STATUS_CODE)

    def get_status_message(self):
        return self.response_params.get(Constants.STATUS_MESSAGE)

    def get_hash_method(self):
        return self.response_params.get(Constants.HASH_METHOD)

    def get_hash(self):
        return self.response_params.get(Constants.HASH)

    def get_merchant_id(self):
        return self.response_params.get(Constants.MERCHANT_ID)

    def get_merchant_key_id(self):
        return self.response_params.get(Constants.MERCHANT_KEY_ID)

    def get_error_code(self):
        return self.response_params.get(Constants.ERROR_CODE)

    def get_error_message(self):
        return self.response_params.get(Constants.ERROR_MESSAGE)

    def is_valid_response(self):
        hash_util = HashUtil(self.response_params, self.response_params.get(Constants.HASH_METHOD))
        return self.response_params.get(Constants.HASH) == hash_util.generate_hash()
