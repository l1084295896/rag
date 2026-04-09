from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 得到模型对象，qwen3—max是聊天模型
model = ChatTongyi(model='qwen3-max')

# 准备消息列表
messages = [SystemMessage(content="你是以为边塞诗人"),
            HumanMessage(content="写一首诗"),
            AIMessage(content="床前明月光，疑是地上霜"),
            HumanMessage(content='按照你上一个的回复格式，再写一首')]

# 调用stream流式执行
res = model.stream(input=messages)

# for 循环迭代打印输出，通过 .content来获取内容
for chunk in res:
    print(chunk.content,end='',flush=True)

