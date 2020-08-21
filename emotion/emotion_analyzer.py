import json
from dotenv import load_dotenv
from os.path import join, dirname
import os
import ctypes.test.test_objects
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibm_watson import LanguageTranslatorV3
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions


def Translate(apiKey, apiUrl, inputText):
    authenticator = IAMAuthenticator(apiKey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(apiUrl)

    translation = language_translator.translate(
        text=inputText,
        model_id='ja-en').get_result()
    # print(translation)
    result = translation['translations'][0]['translation']
    return result


def NaturalLanguageAnalyzer(apiKey, apiUrl, inputText):
    authenticator = IAMAuthenticator(apiKey)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(apiUrl)

    response = natural_language_understanding.analyze(
        text=inputText,
        features=Features(emotion=EmotionOptions())).get_result()

    result = json.dumps(response, indent=2)
    return result


def NaturalLanguageAnalyzerWrapper(translateApiKey, translateApiUrl, analyzerApiKey, analyzerApiurl, inputText):
    english_text = Translate(translateApiKey, translateApiUrl, inputText)
    try:
        result = NaturalLanguageAnalyzer(analyzerApiKey, analyzerApiurl, english_text)
    except ApiException:
        return False
    else:
        return result
