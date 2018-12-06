from qa.settings import GOOGLE_APPLICATION_CREDENTIALS
import jwt
import time
import json


def make_iap_request():
    '''Login method from https://developers.google.com/identity/protocols/OAuth2ServiceAccount'''
    hours = 3600 * 2
    iat = time.time()
    exp = iat + hours
    payload = {
        'iss': '123456-compute@developer.gserviceaccount.com',
        'sub': '123456-compute@developer.gserviceaccount.com',
        'aud': 'https://firestore.googleapis.com/google.firestore.v1beta1.Firestore',
        'iat': iat,
        'exp': exp
    }
    with open(GOOGLE_APPLICATION_CREDENTIALS) as f:
        json_data = json.load(f)
    PRIVATE_KEY_ID_FROM_JSON=json_data['private_key_id']
    PRIVATE_KEY_FROM_JSON=json_data['private_key']
    additional_headers = {'kid': PRIVATE_KEY_ID_FROM_JSON}
    signed_jwt = jwt.encode(payload, PRIVATE_KEY_FROM_JSON, headers=additional_headers, algorithm='RS256')
    bearer_header = 'Bearer %s' % signed_jwt.decode('utf-8')
    return bearer_header
