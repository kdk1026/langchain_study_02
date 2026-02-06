import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai", api_key=gemini_api_key)

try:
    for chunk in model.stream("안녕하세요. 당신은 누구입니까?") :
        print(chunk.text, end="")
except Exception as e:
    if "429" in str(e):
        print("대기 시간이 필요합니다. API 사용량이 초과되었습니다. (잠시 후 다시 시도)")
    else:
        print(f"오류 발생: {e}")
