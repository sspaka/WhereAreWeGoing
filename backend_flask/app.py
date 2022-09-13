from flask import Flask, render_template, jsonify, request
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from konlpy.tag import Kkma, Okt, Komoran

app = Flask(__name__)
api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")  # Flask 객체에 Api 객체 등록

# morph_api = api.namespace('/', description='형태소 분리 API')

kkma = Kkma()
okt = Okt()
komoran = Komoran()


@api.route("/morph")
class Morpheme(Resource):
    @api.doc(params={'text': {'description': '형태소 분리할 문장들', 'type': 'String'}})
    def get(self):
        ''' 문장들을 받아서 형태소로 분리해 반환한다. (중복제외) '''
        text = request.args.get('text')
        # morphs = okt.morphs(text)  # 형태소 추출
        # kkma.sentences(text)  # 문장 분리

        pos = okt.pos(text) # 형태소+품사태그 추출
        # nouns = kkma.nouns(text) # 명사만 추출
        return list(set(pos))

    def post(self):
        '''문장들을 받아서 형태소로 분리해 반환한다. (중복제외) '''
        # text = request.get_json()['text'] # json으로 받을때
        text = request.form.get('text') # form으로 받을 때
        # text = text.encode("utf-8")
        pos = okt.pos(text)  # 형태소+품사태그 추출
        # nouns = kkma.nouns(text) # 명사만 추출
        return list(set(pos))


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
