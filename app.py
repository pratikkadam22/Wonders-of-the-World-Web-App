"""
A flask web app demonstrating information about the Wonders of the World
"""
import flask
from flask.views import MethodView
from flask import redirect, request, url_for, render_template
from google.cloud import vision
from google.cloud import translate
from google.cloud.vision import types
from google.cloud import texttospeech
import six
import os

#setting up a static directory
ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT,'static')

#creates app as a flask object
app = flask.Flask(__name__)

#default landing page using route() method of flask
@app.route('/')
def home():
        return render_template('home.html')

#landing page of webpage for taj
@app.route('/taj')
def taj():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/Taj_Mahal_in_March_2004.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'The Taj Mahal is an ivory-white marble mausoleum on the south bank of the Yamuna river in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor, Shah Jahan, to house the tomb of his favourite wife, Mumtaz Mahal.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'taj' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('taj.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))

#landing page of webpage for the wall
@app.route('/wall')
def wall():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/1024px-The_Great_Wall_of_China_at_Jinshanling-edit.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'The Great Wall of China is a series of fortifications made of stone, brick, tamped earth, wood, and other materials, generally built along an east-to-west line across the historical northern borders of China to protect the Chinese states and empires against the raids and invasions of the various nomadic groups of the Eurasian Steppe with an eye to expansion.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'wall' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('wall.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))

#landing page of webpage for giza
@app.route('/giza')
def giza():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/1024px-Kheops-Pyramid.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'The Great Pyramid of Giza (also known as the Pyramid of Khufu or the Pyramid of Cheops) is the oldest and largest of the three pyramids in the Giza pyramid complex bordering what is now El Giza, Egypt. It is the oldest of the Seven Wonders of the Ancient World, and the only one to remain largely intact.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'giza' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('giza.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))

#landing page of webpage for christ
@app.route('/christ')
def christ():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/christ.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'Christ the Redeemer is an Art Deco statue of Jesus Christ in Rio de Janeiro, Brazil, created by French sculptor Paul Landowski and built by Brazilian engineer Heitor da Silva Costa, in collaboration with French engineer Albert Caquot. Romanian sculptor Gheorghe Leonida fashioned the face.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'christ' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('christ.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))

#landing page of webpage for petra
@app.route('/petra')
def petra():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/The_Monastery,_Petra,_Jordan8.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'Petra, originally known to its inhabitants as Raqmu, is a historical and archaeological city in southern Jordan.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'petra' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('petra.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))

#landing page of webpage for colo
@app.route('/colo')
def colo():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/colosseum.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'The Colosseum is an oval amphitheatre in the centre of the city of Rome, Italy. Built of travertine, tuff, and brick-faced concrete, it is the largest amphitheatre ever built.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'colo' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('colo.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))

#landing page of webpage for chichen
@app.route('/chichen')
def chichen():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/Chichen_Itza_3.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'Chichen Itza was a large pre-Columbian city built by the Maya people of the Terminal Classic period. The archaeological site is located in Tinúm Municipality, Yucatán State, Mexico.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'chichen' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('chichen.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))

#landing page of webpage for machu
@app.route('/machu')
def machu():
		#use of Vision API for landmark detection
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = 'https://storage.googleapis.com/finalpkadam/templates/Machu_Picchu,_Peru.jpg'
        resp = client.landmark_detection(image=image)
        landmarks = resp.landmark_annotations
        for landmark in landmarks:
        	entry = landmark.description
        
        #use of Translate API for translating the description
        text1 = 'Machu Picchu is a 15th-century Inca citadel, located in the Eastern Cordillera of southern Peru, on a mountain ridge 2,430 metres (7,970 ft) above sea level.'
        translate_client = translate.Client()
        if isinstance(text1, six.binary_type):
                text1 = text1.decode('utf-8')
        target1 = 'zh'
        result1 = translate_client.translate(text1, target_language=target1)
        target2 = 'hi'
        result2 = translate_client.translate(text1, target_language=target2)   
        
        #use of TextToSpeech API for audio of the description
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text1)
        voice = texttospeech.types.VoiceSelectionParams(
        	language_code='en-US',
        	ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        audio_config = texttospeech.types.AudioConfig(
        	audio_encoding=texttospeech.enums.AudioEncoding.MP3)	
        response = client.synthesize_speech(input_text, voice, audio_config)
        voice = 'machu' + '.mp3'
        voicepath = os.path.join(STATIC_DIR, voice)
        with open(voicepath, 'wb') as out:
        	out.write(response.audio_content)
        
        #rendering the associated webpage and sending the output values through
        return render_template('machu.html',info = entry, info2 = '{}'.format(result1['translatedText']), info3 = '{}'.format(result2['translatedText']))


#using run() method of flask, launch the web app on all IP addresses of the host using port 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
