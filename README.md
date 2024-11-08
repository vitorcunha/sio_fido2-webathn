# Going Passwordless with py_webauthn (SIO FIDO2/WebAuthn)

A basic demo of WebAuthn RP using the [py_webauthn](https://github.com/duo-labs/py_webauthn) library for passwordless account registration and authentication.

Full credits go to Duo Labs for the [original implementation](https://github.com/duo-labs/duo-blog-going-passwordless-with-py-webauthn).

## Starting the demo

First, you will need to implement the methods in `src/app.py` to have a fully functioning demo.You can set up the virtual environment this way:

```sh
# enter the folder for the server demo code
$ cd fido2-demo

# Create your virtualenv
$ virtualenv venv

# Enter the virtualenv venv
$ source venv/bin/activate

# Install the requirements and their dependencies
$ sudo apt install libffi-dev
$ pip install -r requirements.txt
```

Then, you can run the webapp this way:
```sh
# Run the webapp
$ ./start-server.sh
```

View the demo at http://localhost:5000
