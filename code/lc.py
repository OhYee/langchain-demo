# 引入所需模块和类
from langchain.agents import load_tools  # 引入加载工具函数
from langchain.agents import initialize_agent  # 引入初始化代理函数
from langchain.agents import AgentType  # 引入代理类型类
from langchain.llms import OpenAI  # 引入OpenAI语言模型类



class LangChain():
    def __init__(self):
        self.openai_key = ""
        self.openai_agent = None
    
    def init_openai(self, openai_key):
        self.openai_key = openai_key
        self.openai_llm = OpenAI(temperature=0, openai_api_key=self.openai_key)

        # 加载所需工具，包括serpapi和llm-math
        tools = load_tools(["llm-math"], llm=self.openai_llm)
        # tools = load_tools(["llm-math"], llm=llm)

        # 初始化代理对象，设定代理类型为ZERO_SHOT_REACT_DESCRIPTION，输出详细信息
        self.openai_agent = initialize_agent(tools, self.openai_llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


    def call(self, openai_key, question):
        if openai_key != self.openai_key or self.openai_agent == None:
            self.init_openai(openai_key)
        
        return self.openai_agent(question)

lc = LangChain()