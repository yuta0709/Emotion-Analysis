from os.path import join, dirname
from dotenv import load_dotenv
import os
import emotion


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TRANSLATE_API_KEY=os.environ.get('TRANSLATE_API_KEY')
TRANSLATE_API_URL=os.environ.get('TRANSLATE_API_URL')
LANGUAGE_API_KEY=os.environ.get('LANGUAGE_API_KEY')
LANGUAGE_API_URL = os.environ.get('LANGUAGE_API_URL')
print(emotion.NaturalLanguageAnalyzerWrapper(TRANSLATE_API_KEY,TRANSLATE_API_URL,LANGUAGE_API_KEY,LANGUAGE_API_URL,"今日は気分がいい"))
