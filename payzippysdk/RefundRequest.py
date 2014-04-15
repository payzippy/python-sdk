import httplib
import urllib
import time

import Constants
from HashUtil import HashUtil
import ValidityCheck
from payzippysdk import Config
from payzippysdk.RefundResponse import RefundResponse


class RefundRequest(object):
    def __init__(self):
        self.request_params = {}
        self.set_merchant_id(Config.merchant_id)
        self.set_merchant_key_id(Config.merchant_key_id)
        self.set_hash_method(Config.hash_method)
        self.refund_api_host = Config.refund_url_host
        self.refund_api_path = Config.refund_url_path

    def set_merchant_id(self, merchant_id):
        self.request_params[Constants.MERCHANT_ID] = merchant_id

    def set_merchant_key_id(self, merchant_key_id):
        self.request_params[Constants.MERCHANT_KEY_ID] = merchant_key_id

    def set_hash_method(self, hash_method):
        self.request_params[Constants.HASH_METHOD] = hash_method.upper()

    def set_hash(self, hashval):
        self.request_params[Constants.HASH] = hashval

    def set_timegmt(self):
        self.request_params[Constants.TIMEGMT] = long(round(time.time() * 1000))

    def set_payzippy_sale_transaction_id(self, payzippy_transaction_id):
        self.request_params[Constants.PAYZIPPY_SALE_TRANSACTION_ID] = payzippy_transaction_id

    def set_merchant_transaction_id(self, merchant_transaction_id):
        self.request_params[Constants.MERCHANT_TRANSACTION_ID] = merchant_transaction_id

    def set_refund_amount(self, refund_amount):
        self.request_params[Constants.REFUND_AMOUNT] = refund_amount

    def set_refund_reason(self, refund_reason):
        self.request_params[Constants.REFUND_REASON] = refund_reason

    def set_refunded_by(self, refunded_by):
        self.request_params[Constants.REFUNDED_BY] = refunded_by

    def set_udf1(self, udf1):
        self.request_params[Constants.UDF1] = udf1

    def set_udf2(self, udf2):
        self.request_params[Constants.UDF2] = udf2

    def set_udf3(self, udf3):
        self.request_params[Constants.UDF3] = udf3

    def set_udf4(self, udf4):
        self.request_params[Constants.UDF4] = udf4

    def set_udf5(self, udf5):
        self.request_params[Constants.UDF5] = udf5

    def refund(self):
        try:
            ValidityCheck.validate_refund_params(self.request_params)
        except Exception, e:
            raise Exception("Invalid parameter : " + str(e))
        hash_util = HashUtil(self.request_params, self.request_params.get(Constants.HASH_METHOD))
        self.request_params[Constants.HASH] = hash_util.generate_hash()

        params = urllib.urlencode(self.request_params)
        conn = httplib.HTTPSConnection(self.refund_api_host)
        conn.request(Constants.POST_METHOD, self.refund_api_path, params, Constants.HEADERS)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        return RefundResponse(data)

    def is_valid(self):
        return ValidityCheck.validate_refund_params(self.request_params)
