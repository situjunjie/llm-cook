import getpass
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain_core.documents import Document


"""
熟悉 LangChain 的文档加载器、嵌入和向量存储抽象
"""

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

# 示例文档
documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
]


"""
加载pdf文件
"""
from langchain_community.document_loaders import PyPDFLoader
file_path = './example-datas/nke-10k-2023.pdf'
loader = PyPDFLoader(file_path)

docs = loader.load()
print(f"{docs[0].page_content[:200]}\n")
print(docs[0].metadata)
