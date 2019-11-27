# coding: UTF-8
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LOGIN_EMAIL = os.environ.get("LOGIN_EMAIL")
LOGIN_PASS = os.environ.get("LOGIN_PASS")
