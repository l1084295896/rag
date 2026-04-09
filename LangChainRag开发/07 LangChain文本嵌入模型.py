from langchain_community.embeddings import  DashScopeEmbeddings

# 创建新对象
model = DashScopeEmbeddings()

#不用invoke stream
print(model.embed_query("我喜欢你")) # 单次转换
print(model.embed_documents(["我喜欢你", "我爱你", "晚上吃什么"]))  # 多次转换 传入列表
