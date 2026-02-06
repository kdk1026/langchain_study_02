import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai", api_key=gemini_api_key)

hm_1 = HumanMessage("안녕하세요. 저는 레브레카입니다.")
aim_1 = AIMessage("안녕하세요 레브레카! 어떤 도움이 필요하신가요?")
hm_2 = HumanMessage("제 이름이 뭐라고 했죠?")

messages = [hm_1, aim_1, hm_2]

try:
    response = model.invoke(messages)

    print(f"클래스 타입: {response.__class__.__name__}")
    print(f"데이터: {response}")
except Exception as e:
    if "429" in str(e):
        print("대기 시간이 필요합니다. API 사용량이 초과되었습니다. (잠시 후 다시 시도)")
    else:
        print(f"오류 발생: {e}")
