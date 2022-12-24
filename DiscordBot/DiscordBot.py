import base64
import hashlib
import requests
import random
import string

def generate_code() -> tuple[str,str]:
    #MAL uses plain system so no need for SHA-256
    rand = random.SystemRandom()
    code_verifier = ''.join(rand.choices(string.ascii_letters + string.digits, k=128))
    code_challenge = code_verifier

    return (code_verifier, code_challenge)

code_verifier, code_challenge = generate_code()

provider = "https://myanimelist.net/v1/oauth2/authorize?"
MAL_client_id = "eaf1923739e60e15240f0a22fb5fbfad"
state = "testapp"

def get_auth_fields(client_id):
    resp = requests.get(
        url=provider,
        params={
            "response_type": "code",
            "client_id": client_id,
            "state": state,
            "code_challenge": code_challenge,
            "code_challenge_method": "plain",
        },
        allow_redirects=False
    )


def get_fields(client_id):

    mal = "https://api.myanimelist.net/v2/anime/47917?fields=id,title,broadcast"

    response = requests.get(
    url=mal,
    headers={
        "X-MAL-CLIENT-ID": client_id,
        }
    )

    print (response.status_code)
    return response.json()        

print(get_fields(MAL_client_id))