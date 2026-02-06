import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
lang_smith_api_key = os.getenv('LANG_SMITH_API_KEY')

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = lang_smith_api_key
os.environ["LANGCHAIN_PROJECT"] = "My_First_Agent"

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai", api_key=gemini_api_key)

try:
    response = model.invoke("랭스미스가 무엇인지 한 문장으로 설명해줘.")

    print(f"답변: {response.content}")
except Exception as e:
    if "429" in str(e):
        print("대기 시간이 필요합니다. API 사용량이 초과되었습니다. (잠시 후 다시 시도)")
    else:
        print(f"오류 발생: {e}")
