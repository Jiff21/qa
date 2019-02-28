# from qa.settings import GOOGLE_APPLICATION_CREDENTIALS
# import jwt
# import time
# import json
#
#
# def make_iap_request():
#     '''Login method from https://developers.google.com/identity/protocols/OAuth2ServiceAccount'''
#     hours = 3600 * 2
#     iat = time.time()
#     exp = iat + hours
#     payload = {
#         'iss': '123456-compute@developer.gserviceaccount.com',
#         'sub': '123456-compute@developer.gserviceaccount.com',
#         'aud': 'https://firestore.googleapis.com/google.firestore.v1beta1.Firestore',
#         'iat': iat,
#         'exp': exp
#     }
#     with open(GOOGLE_APPLICATION_CREDENTIALS) as f:
#         json_data = json.load(f)
#     PRIVATE_KEY_ID_FROM_JSON=json_data['private_key_id']
#     PRIVATE_KEY_FROM_JSON=json_data['private_key']
#     additional_headers = {'kid': PRIVATE_KEY_ID_FROM_JSON}
#     signed_jwt = jwt.encode(payload, PRIVATE_KEY_FROM_JSON, headers=additional_headers, algorithm='RS256')
#     bearer_header = 'Bearer %s' % signed_jwt.decode('utf-8')
#     return bearer_header
from qa.settings import ALLURE_REPORT_HUB_URL, ALLURE_HUB_CLIENT_ID
import jwt #PyJWT==1.6.4
import time
import json


def make_iap_request(credential_file_path):
    '''Login method from https://developers.google.com/identity/protocols/OAuth2ServiceAccount'''
    iap_project_number = '' #Get these from IAP three dots
    iap_project_name = ''
    expected_audience = '/projects/{}/apps/{}'.format(
            iap_project_number, iap_project_name)
    hours = 3600 * 2
    iat = time.time()
    exp = iat + hours
    payload = {
        'iss': 'https://cloud.google.com/iap',
        'sub': ALLURE_HUB_CLIENT_ID,
        # 'hd': ALLURE_REPORT_HUB_URL # Need to get a HOST version?
        'aud': expected_audience,
        'iat': iat,
        'exp': exp
    }
    with open(credential_file_path) as f:
        json_data = json.load(f)
    PRIVATE_KEY_ID_FROM_JSON=json_data['private_key_id']
    PRIVATE_KEY_FROM_JSON=json_data['private_key']
    additional_headers = {'kid': PRIVATE_KEY_ID_FROM_JSON}
    signed_jwt = jwt.encode(payload, PRIVATE_KEY_FROM_JSON, headers=additional_headers, algorithm='RS256')
    bearer_header = 'Bearer %s' % signed_jwt.decode('utf-8')
    return bearer_header
