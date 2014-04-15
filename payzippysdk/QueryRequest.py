import httplib
import urllib

import Constants
from HashUtil import HashUtil
import ValidityCheck
from payzippysdk import Config
from payzippysdk.QueryResponse import QueryResponse


class QueryRequest(object):
    """
    Class use to create the _query_request object
    """

    def __init__(self):
        self.query_params = {}
        self.set_merchant_id(Config.merchant_id)
        self.set_merchant_key_id(Config.merchant_key_id)
        self.set_hash_method(Config.hash_method)
        self.query_api_host = Config.query_url_host
        self.query_api_path = Config.query_url_path

    def set_merchant_id(self, merchant_id):
        self.query_params[Constants.MERCHANT_ID] = merchant_id

    def set_merchant_key_id(self, merchant_key_id):
        self.query_params[Constants.MERCHANT_KEY_ID] = merchant_key_id

    def set_payzippy_transaction_id(self, payzippy_transaction_id):
        self.query_params[Constants.PAYZIPPY_TRANSACTION_ID] = payzippy_transaction_id

    def set_hash_method(self, hash_method):
        self.query_params[Constants.HASH_METHOD] = hash_method

    def set_hash(self, hashval):
        self.query_params[Constants.HASH] = hashval

    def set_merchant_transaction_id(self, merchant_transaction_id):
        self.query_params[Constants.MERCHANT_TRANSACTION_ID] = merchant_transaction_id

    def set_transaction_type(self, transaction_type):
        self.query_params[Constants.TRANSACTION_TYPE] = transaction_type

    def query(self):
        try:
            ValidityCheck.validate_query_params(self.query_params)
        except Exception, e:
            raise Exception("Invalid parameter : " + str(e))
        else:
            hash_util = HashUtil(self.query_params, self.query_params.get(Constants.HASH_METHOD))
            self.query_params[Constants.HASH] = hash_util.generate_hash()

            params = urllib.urlencode(self.query_params)
            conn = httplib.HTTPSConnection(self.query_api_host)
            conn.request(Constants.POST_METHOD, self.query_api_path, params, Constants.HEADERS)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        return QueryResponse(data)
