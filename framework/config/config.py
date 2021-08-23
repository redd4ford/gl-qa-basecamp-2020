import os


class Config:
    BASE_URL = os.getenv('TESTBASE_URL', 'https://reqres.in')
    # prod - https://reqres.in
    # qa - https://qa.reqres.in
    # dev - https://dev.reqres.in
