from langchain_community.llms.tongyi import Tongyi

model=Tongyi(model='qwen-max')

#通过stream方法获得流式输出
res=model.stream(input='你是谁，你能做什么呢？')  # 不直接打印res是因为res是迭代器

for chunk in res:
    print(chunk,end='',flush=True)
