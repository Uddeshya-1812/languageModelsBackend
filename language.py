import re
import pickle
model = pickle.load(open('./model.pkl', 'rb'))
cv = pickle.load(open('./cv.pkl', 'rb'))
le = pickle.load(open('./le.pkl', 'rb'))

def preprocessText(text):
    text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    text = text.lower()
    return text

def getLanguageId(text):
    try:
        text = preprocessText(text)
        textArray = cv.transform([text]).toarray()
        language = model.predict(textArray)
        language = le.inverse_transform(language)
        languageId = {
            'text': text,
            'id': language[0]
        }

        return languageId
    except Exception as e:
        print(e)
        return {
            'text': text,
            'id': 'Unable to predict ' + str(e)
        }
