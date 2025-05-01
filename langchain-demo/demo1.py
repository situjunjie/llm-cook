from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate

# 加载.env文件中的环境变量
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


# 配置ChatOpenAI使用deepseek模型
chat = ChatOpenAI(
    model_name="deepseek-chat",
    openai_api_key=OPENAI_API_KEY,
    openai_api_base="https://api.deepseek.com",
    temperature=0.0
)

# 简单测试
from langchain_core.messages import HumanMessage

messages = [HumanMessage(content="你好，请介绍一下自己")]
response = chat.invoke(messages)
print(response.content)

# 使用ChatPromptTemplate示例
template = ChatPromptTemplate.from_messages([
    ("system", "你是一个有帮助的AI助手。"),
    ("human", "{input}")
])

chain = template | chat
response = chain.invoke({"input": "介绍一下中国的历史"})
print(response.content)

