import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# 加载.env文件中的环境变量
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.deepseek.com")

def getClient():
    return client

# 一个封装 OpenAI 接口的函数，参数为 Prompt，返回对应结果
def get_completion(prompt, model="deepseek-chat"):
    '''
    prompt: 对应的提示词
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
    '''
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # 模型输出的温度系数，控制输出的随机程度
        stream=False
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message.content



def get_completion_from_messages(messages, max_tokens=1000, model="deepseek-chat", temperature=0):
    response = getClient().chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature, # 控制模型输出的随机程度
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message.content



