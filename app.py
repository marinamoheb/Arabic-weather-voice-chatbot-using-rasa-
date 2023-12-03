from flask import render_template,Flask,request,jsonify
import requests
from playsound import playsound
from translate import Translator

RASA_API_URL ='http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)


# # # @app.route("/")
# # # def index():  
# # #     return render_template('index.html')

# # # @app.route('/webhook',methods=['POST'])
# # # def webhook():
# # #     user_message = request.json['message']
# # #     print("User Message:", user_message)

# # #     rasa_response=requests.post(RASA_API_URL, json={'message': user_message})
# # #     rasa_response_json = rasa_response_json()

# # #     print("Rasa Response:", rasa_response_json)

# # #     bot_response= rasa_response_json[0]['text'] if rasa_response_json else 'Sorry,I did not understand that'
# # #     return jsonify({'response': bot_response})
import requests
import speech_recognition as sr     # import the library
import os
from gtts import gTTS
from playsound import playsound
@app.route('/')
def index():  
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
# bot_response = ""
# user_message=""
def webhook():
    #   user_message = request.json['message']
    #   print("User Message:", user_message)
      translator=Translator(to_lang='ar')
      r = sr.Recognizer()  # initialize recognizer
      with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(translator.translate(message)))
        print("You said : {}".format(message))
        user_message=translator.translate(message)
        # user_message = request.json['message']
        print("User Message:", user_message)








      translator=Translator(to_lang='ar')
      
      rasa_response=requests.post(RASA_API_URL, json={'message': user_message
      })
      rasa_response_json = rasa_response.json()

      print("Rasa Response:", rasa_response_json)

      bot_response= rasa_response_json[0]['text'] if rasa_response_json else 'Sorry,I didn\t understand that.'
      print(bot_response)
      myobj = gTTS(text=translator.translate(bot_response),lang='ar')
      myobj.save("welcome.mp3")
      print('saved')
      playsound('welcome.mp3')
      os.remove("welcome.mp3")
      return jsonify({'response': bot_response})

if __name__ == "__main__":  
    app.run(debug=True,port=3000)