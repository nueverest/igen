import os
from dotenv import load_dotenv


# set api key in env or in llm
load_dotenv()
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
STABLE_API_KEY = os.getenv("STABLE_API_KEY")

# # local env variable
# TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
