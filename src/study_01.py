import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
os.environ["GOOGLE_API_KEY"] = gemini_api_key

"""
    https://reference.langchain.com/python/langchain/models/

    docs 폴더의 "init_chat_model 파라미터.md" 참고 (구글 AI 개요)
"""
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

try:
    response = model.invoke("안녕하세요. 당신은 누구입니까?")
    # print(response)
    print(response.content)

    print(response.usage_metadata)
except Exception as e:
    if "429" in str(e):
        print("대기 시간이 필요합니다. API 사용량이 초과되었습니다. (잠시 후 다시 시도)")
    else:
        print(f"오류 발생: {e}")
