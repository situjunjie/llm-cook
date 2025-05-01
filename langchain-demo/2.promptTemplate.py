"""
学习怎么使用promptTempalte
"""
import getpass
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
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

# 系统消息模板
system_template = "Translate the following from English into {language}"

# 构建消息模板 prompt_template
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
prompt = prompt_template.invoke({"language": "Chinese", "text": "hi!"})
# invoke 生成了prompt对象，用于准备传递给llm
print('promt.to_messages:',prompt.to_messages())
# 拿去调用模型看看
response = llm.invoke(prompt)
print(response.content)