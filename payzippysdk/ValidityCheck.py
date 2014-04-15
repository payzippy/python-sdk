import Constants


# =================================================
# Query Parameters Validation
# =================================================
def validate_query_params(params):
    param_keys = list(params.keys())

    if not bool(params.get(Constants.MERCHANT_ID)) or len(
            params.get(Constants.MERCHANT_ID)) > Constants.MERCHANT_ID_MAXLEN:
        raise ValueError(Constants.MERCHANT_ID_INVALID)

    elif not bool(params.get(Constants.MERCHANT_KEY_ID)) or len(
            params.get(Constants.MERCHANT_KEY_ID)) > Constants.MERCHANT_KEY_ID_MAXLEN:
        raise ValueError(Constants.MERCHANT_KEY_ID_INVALID)

    elif not Constants.PAYZIPPY_TRANSACTION_ID in param_keys and (
            not bool(params.get(Constants.MERCHANT_TRANSACTION_ID))
            or len(params.get(Constants.MERCHANT_TRANSACTION_ID)) > Constants.PAYZIPPY_TRANSACTION_ID_MAXLEN):
        raise ValueError(Constants.MERCHANT_TRANSACTION_ID_INVALID)

    elif not Constants.MERCHANT_TRANSACTION_ID in param_keys and (
            not bool(params.get(Constants.PAYZIPPY_TRANSACTION_ID))
            or len(params.get(Constants.PAYZIPPY_TRANSACTION_ID)) > Constants.MERCHANT_TRANSACTION_ID_MAXLEN):
        raise ValueError(Constants.PAYZIPPY_SALE_TRANSACTION_ID_INVALID)

    elif params.get(Constants.HASH_METHOD).upper() not in Constants.HASH_METHOD_REQUIREMENTS or not bool(
            params.get(Constants.HASH_METHOD)):
        raise ValueError(Constants.HASH_METHOD_INVALID)

    elif Constants.TRANSACTION_TYPE in param_keys and bool(params.get(Constants.TRANSACTION_TYPE)) and len(
            params.get(Constants.TRANSACTION_TYPE)) > Constants.TRANSACTION_TYPE_MAXLEN:
        raise ValueError(Constants.TRANSACTION_TYPE_INVALID)

    elif Constants.TRANSACTION_TYPE in param_keys and (
            not bool(params.get(Constants.TRANSACTION_TYPE)) or params.get(Constants.TRANSACTION_TYPE)
            not in Constants.SALE_REFUND_LIST):
        raise ValueError(Constants.TRANSACTION_TYPE_INVALID)

    else:
        return True


# =================================================
# Charging Parameters Validation
# =================================================
def validate_charge_params(params):
    param_keys = list(params.keys())
    # '''
    # mandatory charging parameters validation
    # '''
    if not bool(params.get(Constants.MERCHANT_ID)) or len(
            params.get(Constants.MERCHANT_ID)) > Constants.MERCHANT_ID_MAXLEN:
        raise ValueError(Constants.MERCHANT_ID_INVALID)

    elif not bool(params.get(Constants.BUYER_EMAIL_ADDRESS)) or len(
            params.get(Constants.BUYER_EMAIL_ADDRESS)) > Constants.BUYER_EMAIL_ADDRESS_MAXLEN:
        raise ValueError(Constants.EMAIL_ADDRESS_INVALID)

    elif not bool(params.get(Constants.MERCHANT_TRANSACTION_ID)) or len(
            params.get(Constants.MERCHANT_TRANSACTION_ID)) > Constants.MERCHANT_TRANSACTION_ID:
        raise ValueError(Constants.MERCHANT_TRANSACTION_ID_INVALID)

    elif not bool(params.get(Constants.TRANSACTION_TYPE)):
        raise ValueError(Constants.TRANSACTION_TYPE_INVALID)

    elif not bool(params.get(Constants.TRANSACTION_AMOUNT)) or not params.get(
            Constants.TRANSACTION_AMOUNT).isdigit() or params.get(Constants.TRANSACTION_AMOUNT) <= 0:
        raise ValueError(Constants.TRANSACTION_AMOUNT_INVALID)

    elif not bool(params.get(Constants.MERCHANT_KEY_ID)) or len(
            params.get(Constants.MERCHANT_KEY_ID)) > Constants.MERCHANT_KEY_ID_MAXLEN:
        raise ValueError(Constants.MERCHANT_ID_INVALID)

    elif (params.get(Constants.UI_MODE) not in Constants.UI_MODE_REQUIREMENTS) or not bool(
            params.get(Constants.UI_MODE)):
        raise ValueError(Constants.UI_MODE_INVALID)

    elif not bool(params.get(Constants.HASH_METHOD)) or not (
            params.get(Constants.HASH_METHOD).upper() in Constants.HASH_METHOD_REQUIREMENTS):
        raise ValueError(Constants.HASH_METHOD_INVALID)

    # '''
    # Check for payment method specific parameters
    # '''

    elif not bool(params.get(Constants.PAYMENT_METHOD)) or not (
            params.get(Constants.PAYMENT_METHOD) in Constants.VALID_PAYMENT_METHODS):
        raise ValueError(Constants.PAYMENT_METHOD_INVALID)

    elif bool(params.get(Constants.PAYMENT_METHOD)) and params.get(
            Constants.PAYMENT_METHOD) is Constants.PAYMENT_MODE_EMI:
        if not bool(params.get(Constants.EMI_MONTHS)) or not (params.get(Constants.EMI_MONTHS).isdigit()) or params.get(
                Constants.EMI_MONTHS) <= 0:
            raise ValueError(Constants.EMI_MONTHS_INVALID)
        if not bool(params.get(Constants.BANK_NAME)) or len(
                params.get(Constants.BANK_NAME)) > Constants.BANK_NAME_MAXLEN:
            raise ValueError(Constants.BANK_NAME_INVALID)

    elif bool(params.get(Constants.PAYMENT_METHOD)) and params.get(
            Constants.PAYMENT_METHOD) is Constants.PAYMENT_MODE_NET:
        if not bool(params.get(Constants.BANK_NAME)) or len(
                params.get(Constants.BANK_NAME)) > Constants.BANK_NAME_MAXLEN:
            raise ValueError(Constants.BANK_NAME_INVALID)

    elif bool(params.get(Constants.PAYMENT_METHOD)) and params.get(
            Constants.PAYMENT_METHOD) is Constants.PAYMENT_MODE_CARD_CAPTURE:
        if not bool(params.get(Constants.CARD_NUMBER)) or not (
            params.get(Constants.CARD_NUMBER).isdigit()) or params.get(Constants.CARD_NUMBER) <= 0 or len(
                params.get(Constants.CARD_NUMBER)) > Constants.CARD_NUMBER_MAXLEN:
            raise ValueError(Constants.CARD_NUMBER_INVALID)
        if not bool(params.get(Constants.CVV)) or not (params.get(Constants.CVV).isdigit()) or params.get(
                Constants.CVV) <= 0 or len(params.get(Constants.CVV)) > Constants.CVV_MAXLEN:
            raise ValueError(Constants.CVV_INVALID)
        if not bool(params.get(Constants.EXPIRY_MONTH)) or not (
            params.get(Constants.EXPIRY_MONTH).isdigit()) or params.get(Constants.EXPIRY_MONTH) <= 0 or len(
                params.get(Constants.EXPIRY_MONTH)) > Constants.EXPIRY_MONTH_MAXLEN:
            raise ValueError(Constants.EXPIRY_MONTH_INVALID)
        if not bool(params.get(Constants.EXPIRY_YEAR)) or not (
            params.get(Constants.EXPIRY_YEAR).isdigit()) or params.get(Constants.EXPIRY_YEAR) <= 0 or len(
                params.get(Constants.EXPIRY_YEAR)) > Constants.EXPIRY_YEAR_MAXLEN:
            raise ValueError(Constants.EXPIRY_YEAR_INVALID)

    # Check for other parameters which enforce max length constraint
    elif Constants.BUYER_PHONE_NO in param_keys and len(
            params.get(Constants.BUYER_PHONE_NO)) > Constants.BUYER_PHONE_NO_MAXLEN:
        raise ValueError(Constants.BUYER_PHONE_NO_INVALID)

    elif Constants.BUYER_UNIQUE_ID in param_keys and len(
            params.get(Constants.BUYER_UNIQUE_ID)) > Constants.BUYER_UNIQUE_ID_MAXLEN:
        raise ValueError(Constants.BUYER_UNIQUE_ID_INVALID)

    elif Constants.SOURCE in param_keys and len(params.get(Constants.SOURCE)) > Constants.SOURCE_MAXLEN:
        raise ValueError(Constants.SOURCE_INVALID)

    elif Constants.CALLBACK_URL in param_keys and len(
            params.get(Constants.CALLBACK_URL)) > Constants.CALLBACK_URL_MAXLEN:
        raise ValueError(Constants.CALLBACK_URL_INVALID)

    elif (Constants.TERMINAL_ID in param_keys) and len(
            params.get(Constants.TERMINAL_ID)) > Constants.TERMINAL_ID_MAXLEN:
        raise ValueError(Constants.UDF1_INVALID)

    else:
        return True


# =================================================
# Refund Parameters Validation
# =================================================
def validate_refund_params(params):
    param_keys = list(params.keys())
    if not bool(params.get(Constants.MERCHANT_ID)) or len(
            params.get(Constants.MERCHANT_ID)) > Constants.MERCHANT_ID_MAXLEN:
        raise ValueError(Constants.MERCHANT_ID_INVALID)

    elif not bool(params.get(Constants.MERCHANT_KEY_ID)) or len(
            params.get(Constants.MERCHANT_KEY_ID)) > Constants.MERCHANT_KEY_ID_MAXLEN:
        raise ValueError(Constants.MERCHANT_KEY_ID_INVALID)

    elif not Constants.PAYZIPPY_SALE_TRANSACTION_ID in param_keys and (
            not bool(params.get(Constants.MERCHANT_TRANSACTION_ID))
            or len(params.get(Constants.MERCHANT_TRANSACTION_ID)) > Constants.PAYZIPPY_SALE_TRANSACTION_ID_MAXLEN):
        raise ValueError(Constants.MERCHANT_TRANSACTION_ID_INVALID)

    elif not Constants.MERCHANT_TRANSACTION_ID in param_keys and (
            not bool(params.get(Constants.PAYZIPPY_SALE_TRANSACTION_ID))
            or len(params.get(Constants.PAYZIPPY_SALE_TRANSACTION_ID)) > Constants.MERCHANT_TRANSACTION_ID_MAXLEN):
        raise ValueError(Constants.PAYZIPPY_SALE_TRANSACTION_ID_INVALID)

    elif not bool(params.get(Constants.REFUND_AMOUNT)) or not (
            params.get(Constants.REFUND_AMOUNT).isdigit()):
        raise ValueError(Constants.REFUND_AMOUNT_INVALID)

    elif not bool(params.get(Constants.HASH_METHOD)) or not (params.get(Constants.HASH_METHOD).upper()
                                                             in Constants.HASH_METHOD_REQUIREMENTS):
        raise ValueError(Constants.HASH_METHOD_INVALID)

    elif (Constants.REFUND_REASON in param_keys) and len(
            params.get(Constants.REFUND_REASON)) > Constants.REFUND_REASON_MAXLEN:
        raise ValueError(Constants.REFUND_REASON_INVALID)

    elif (Constants.REFUNDED_BY in param_keys) and len(
            params.get(Constants.REFUNDED_BY)) > Constants.REFUNDED_BY_MAXLEN:
        raise ValueError(Constants.REFUNDED_BY_INVALID)

    elif (Constants.TIMEGMT in param_keys) and len(
            params.get(Constants.TIMEGMT)) != Constants.TIMEGMT_MAXLEN:
        raise ValueError(Constants.TIMEGMT_INVALID)

    elif (Constants.UDF1 in param_keys) and len(params.get(Constants.UDF1)) > Constants.UDF1_MAXLEN:
        raise ValueError(Constants.UDF1_INVALID)

    elif (Constants.UDF2 in param_keys) and len(params.get(Constants.UDF2)) > Constants.UDF2_MAXLEN:
        raise ValueError(Constants.UDF2_INVALID)

    elif (Constants.UDF3 in param_keys) and len(params.get(Constants.UDF3)) > Constants.UDF3_MAXLEN:
        raise ValueError(Constants.UDF3_INVALID)

    elif (Constants.UDF4 in param_keys) and len(params.get(Constants.UDF4)) > Constants.UDF4_MAXLEN:
        raise ValueError(Constants.UDF4_INVALID)

    elif (Constants.UDF5 in param_keys) and len(params.get(Constants.UDF5)) > Constants.UDF5_MAXLEN:
        raise ValueError(Constants.UDF5_INVALID)
    else:
        return True
