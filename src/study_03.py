import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai", api_key=gemini_api_key)

inputs = [
    "과적합이 뭔가요?",
    "앵무새의 털 색상이 화려하 이유는?",
    "AI Agent 기반 서비스는 뭐가 있나요?"
]

try:
    responses = model.batch(inputs)

    for response in responses:
        print(response)
except Exception as e:
    if "429" in str(e):
        print("대기 시간이 필요합니다. API 사용량이 초과되었습니다. (잠시 후 다시 시도)")
    else:
        print(f"오류 발생: {e}")
