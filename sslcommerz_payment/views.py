import json
import random
import string
from pprint import pprint
import hashlib

import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from sslcommerz_payment.models import SslcommerzCredential, SslcommerzInformation


class SSLCommerz_payment:
    __CREDENTIAL = {}
    __GW_PROCESS_URL = '/gwprocess/v3/api.php'
    __VALIDATION_URL = '/validator/api/validationserverAPI.php'
    __REFUND_URL = '/validator/api/merchantTransIDvalidationAPI.php'
    __CURRENCY = "BDT"
    __EMI = 0

    def __init__(self):
        credential_model_obj = SslcommerzCredential.objects.last()
        self.__CREDENTIAL = {
            "id": credential_model_obj.id,
            "active_payment": credential_model_obj.active_payment,
            "live_base_url": credential_model_obj.live_base_url,
            "sandbox_base_url": credential_model_obj.sandbox_base_url,
            "live_store_name": credential_model_obj.live_store_name,
            "live_store_id": credential_model_obj.live_store_id,
            "live_store_pass": credential_model_obj.live_store_pass,
            "sandbox_store_name": credential_model_obj.sandbox_store_name,
            "sandbox_store_id": credential_model_obj.sandbox_store_id,
            "sandbox_store_pass": credential_model_obj.sandbox_store_pass,
            "success_url": credential_model_obj.success_url,
            "fail_url": credential_model_obj.fail_url,
            "cancel_url": credential_model_obj.cancel_url,
            "gw_process_url": credential_model_obj.sandbox_base_url + self.__GW_PROCESS_URL if credential_model_obj.active_payment == "sandbox" else credential_model_obj.live_base_url + self.__GW_PROCESS_URL,
            "validation_url": credential_model_obj.sandbox_base_url + self.__VALIDATION_URL if credential_model_obj.active_payment == "sandbox" else credential_model_obj.live_base_url + self.__VALIDATION_URL,
            "refund_url": credential_model_obj.sandbox_base_url + self.__REFUND_URL if credential_model_obj.active_payment == "sandbox" else credential_model_obj.live_base_url + self.__REFUND_URL,
            "currency": self.__CURRENCY,
        }

    # to api request and response process
    def __api_process(self, method="POST", url=None, data=None):
        if url is not None and data is not None and len(data) > 0:
            headers = {
                'Accept': 'application/json',
                'content-type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache",
            }
            if method == "POST":
                res = requests.request(method, url, data=data, headers=headers)
            else:
                res = requests.request(method, url, params=data, headers=headers)

            if res.status_code == 200:
                return res.json()
            else:
                return False
        return False

    # to generate random alpha numeric string for transaction id
    def __get_random_string(self, length=8):
        chars = string.ascii_letters + string.digits
        return ''.join((random.choice(chars)) for _ in range(length))

    # first gateway api call
    def gateway_process(self, cus_name=None, cus_email=None, cus_phone=None, total_amount=None, extra_data_a=None, extra_data_b=None, extra_data_c=None):
        msg_type = False
        msg = ""
        detail = {}

        if cus_name is not None and cus_email is not None and cus_phone is not None and total_amount is not None:
            url = self.__CREDENTIAL['gw_process_url']
            data = {
                'store_id': self.__CREDENTIAL['sandbox_store_id'] if self.__CREDENTIAL['active_payment'] == "sandbox" else self.__CREDENTIAL['live_store_id'],
                'store_passwd': self.__CREDENTIAL['sandbox_store_pass'] if self.__CREDENTIAL['active_payment'] == "sandbox" else self.__CREDENTIAL['live_store_pass'],
                'total_amount': total_amount,
                'currency': self.__CREDENTIAL['currency'],
                'tran_id': self.__get_random_string(12),
                'success_url': self.__CREDENTIAL['success_url'],
                'fail_url': self.__CREDENTIAL['fail_url'],
                'cancel_url': self.__CREDENTIAL['cancel_url'],
                'cus_name': cus_name,
                'cus_email': cus_email,
                'cus_phone': cus_phone,
                'value_a': extra_data_a,
                'value_b': extra_data_b,
                'value_c': extra_data_c
            }

            api_process_res = self.__api_process(url=url, data=data)
            if api_process_res is not False:
                msg_type = True
                msg = "Successfully fetched api response."
                detail = api_process_res

            else:
                msg_type = False
                msg = "Problem to connect/process 'gwprocess' api!"
                detail = {}

        else:
            msg_type = False
            msg = "Required data are missing!"
            detail = {}

        return {"msg_type": msg_type, "msg": msg, "detail": detail}

    # hash verification after first gateway api call
    def hash_verify(self, ssl_response=None):
        if ssl_response is not None and ssl_response['verify_sign'] is not None and ssl_response['verify_key'] is not None:
            verify_key_list = ssl_response['verify_key'].split(',')

            # getting values by verify key after splitting by (,)
            new_data = {}
            if len(verify_key_list) > 0:
                for verify_key_index in verify_key_list:
                    if ssl_response[verify_key_index] is not None:
                        new_data[verify_key_index] = ssl_response[verify_key_index]

            # md5 of store password
            new_data['store_passwd'] = hashlib.md5(self.__CREDENTIAL['sandbox_store_pass'].encode('utf-8')).hexdigest() if self.__CREDENTIAL['active_payment'] == "sandbox" else hashlib.md5(self.__CREDENTIAL['live_store_pass'].encode('utf-8')).hexdigest()

            # sorting
            new_data_sorted = {}
            for key in sorted(new_data):
                new_data_sorted[key] = new_data[key]

            hash_str = "&".join("=".join(_) for _ in new_data_sorted.items())

            if hashlib.md5(hash_str.encode('utf-8')).hexdigest() == ssl_response['verify_sign']:
                return True
            return False
        return False

    # to order validation
    def order_validate(self, validation_id=None):
        msg_type = False
        msg = ""
        detail = {}

        if validation_id is not None:
            url = self.__CREDENTIAL['validation_url']
            data = {
                'store_id': self.__CREDENTIAL['sandbox_store_id'] if self.__CREDENTIAL['active_payment'] == "sandbox" else self.__CREDENTIAL['live_store_id'],
                'store_passwd': self.__CREDENTIAL['sandbox_store_pass'] if self.__CREDENTIAL['active_payment'] == "sandbox" else self.__CREDENTIAL['live_store_pass'],
                'val_id': validation_id,
                'v': 1,
                'format': 'json'
            }

            api_process_res = self.__api_process(method="GET", url=url, data=data)
            if api_process_res is not False:
                msg_type = True
                msg = "Successfully fetched order validation response."
                detail = api_process_res

            else:
                msg_type = False
                msg = "Problem to connect/process 'validationserverAPI.php' api!"
                detail = {}

        else:
            msg_type = False
            msg = "Required data are missing!"
            detail = {}

        return {"msg_type": msg_type, "msg": msg, "detail": detail}

