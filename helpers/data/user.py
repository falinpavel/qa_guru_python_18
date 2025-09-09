import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class User:
    USER_LOGIN = os.getenv("EMAIL")
    USER_PASSWORD = os.getenv("PASSWORD")
