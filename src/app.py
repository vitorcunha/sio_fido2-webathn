from typing import Dict
import json

from flask import Flask, render_template, request
from webauthn import (
    generate_registration_options,
    verify_registration_response,
    generate_authentication_options,
    verify_authentication_response,
    options_to_json,
)
from webauthn.helpers.structs import (
    AuthenticatorSelectionCriteria,
    UserVerificationRequirement,
    RegistrationCredential,
    AuthenticationCredential,
)
from webauthn.helpers.cose import COSEAlgorithmIdentifier

from .models import Credential, UserAccount


# Create our Flask app
app = Flask(__name__)

################
#
# RP Configuration
#
################

rp_id = "localhost"
origin = "http://localhost:5000"
rp_name = "Sample RP"
user_id = "some_random_user_identifier_like_a_uuid"
username = f"your.name@{rp_id}"
print(f"User ID: {user_id}")
print(f"Username: {username}")

# A simple way to persist credentials by user ID
in_memory_db: Dict[str, UserAccount] = {}

# Register our sample user
in_memory_db[user_id] = UserAccount(
    id=user_id,
    username=username,
    credentials=[],
)

# Passwordless assumes you're able to identify the user before performing registration or
# authentication
logged_in_user_id = user_id

# A simple way to persist challenges until response verification
current_registration_challenge = None
current_authentication_challenge = None


################
#
# Views
#
################


@app.route("/")
def index():
    context = {
        "username": username,
    }
    return render_template("index.html", **context)


################
#
# Registration
#
################


@app.route("/generate-registration-options", methods=["GET"])
def handler_generate_registration_options():
    global current_registration_challenge
    global logged_in_user_id

    user = in_memory_db[logged_in_user_id]

    # TODO: implement me!

    return options_to_json(options)


@app.route("/verify-registration-response", methods=["POST"])
def handler_verify_registration_response():
    global current_registration_challenge
    global logged_in_user_id

    body = request.get_data()

    # TODO: implement me!

    # !! Warning: default return may be changed here !!
    return {"verified": False}


################
#
# Authentication
#
################


@app.route("/generate-authentication-options", methods=["GET"])
def handler_generate_authentication_options():
    global current_authentication_challenge
    global logged_in_user_id

    user = in_memory_db[logged_in_user_id]

    # TODO: implement me!

    return options_to_json(options)


@app.route("/verify-authentication-response", methods=["POST"])
def hander_verify_authentication_response():
    global current_authentication_challenge
    global logged_in_user_id

    body = request.get_data()

    # TODO: implement me!

    # !! Warning: default return may be changed here !!
    return {"verified": False}
