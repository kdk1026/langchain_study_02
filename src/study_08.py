import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai", api_key=gemini_api_key)

"""
    role
        system = SystemMessage
        user / human = HumanMessage
        ai / assistant = AIMessage
"""
messages = [
    {"role": "system", "content": "당신은 유능한 로켓 전문가입니다."},
    {"role": "human", "content": "안녕하세요. 궁금한 게 있어요!"},
    {"role": "ai", "content": "로켓 관련 무엇이든 물어보세요."},
    {"role": "human", "content": "추진 방식 차이를 설명해 주세요"},
]

try:
    response = model.invoke(messages)

    print(f"클래스 타입: {response.__class__.__name__}")
    print(f"데이터: {response}")
except Exception as e:
    if "429" in str(e):
        print("대기 시간이 필요합니다. API 사용량이 초과되었습니다. (잠시 후 다시 시도)")
    else:
        print(f"오류 발생: {e}")
