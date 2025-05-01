"""
学习使用怎么实例化model，使用deepseek模型
"""

import getpass
import os
from dotenv import load_dotenv

from langchain_deepseek import ChatDeepSeek

# 加载.env文件中的环境变量
load_dotenv()

if not os.getenv("DEEPSEEK_API_KEY"):
    os.environ["DEEPSEEK_API_KEY"] = getpass.getpass("Enter your DeepSeek API key: ")

# 实例化deepseek模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    max_retries=2,
    # other params...
)

# 使用列表消息
# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to Chinese. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# ai_msg = llm.invoke(messages)
# ai_msg.content
# print(ai_msg.content)

from langchain_core.messages import HumanMessage, SystemMessage
# 使用SystemMessage和HumanMessage
messages = [
    SystemMessage("Translate the following from English into Chinese"),
    HumanMessage("hi!,My name is John"),
]

# 普通调用同步输出
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)

# 同步流式输出：
for token in llm.stream(messages):
    print(token.content, end="|")


# 