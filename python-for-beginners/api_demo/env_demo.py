# Import the os module and load_dotenv method
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Print out the API_KEY
api_key = os.getenv('API_KEY')
print(api_key)
