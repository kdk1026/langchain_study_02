import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai", api_key=gemini_api_key)

json_schema = {
    "title": "Movie",
    "description": "상세한 영화 정보.",
    "type": "object",
    "properties": {
        "title": {
            "title": "Title",
            "description": "영화의 제목",
            "type": "string"
        },
        "year": {
            "title": "Year",
            "description": "개봉 연도",
            "type": "integer"
        },
        "director": {
            "title": "Director",
            "description": "영화 감독 이름",
            "type": "string"
        },
        "rating": {
            "title": "Rating",
            "description": "영화 평점 (10점 만점)",
            "type": "number"
        }
    },
    "required": ["title", "year", "director", "rating"]
}

model_with_json_schema = model.with_structured_output(json_schema)

try:
    response = model_with_json_schema.invoke("영화 인셉션에 대해 설명해 주세요.")

    print(f"클래스 타입: {response.__class__.__name__}")
    print(f"데이터: {response}")
except Exception as e:
    if "429" in str(e):
        print("대기 시간이 필요합니다. API 사용량이 초과되었습니다. (잠시 후 다시 시도)")
    else:
        print(f"오류 발생: {e}")
