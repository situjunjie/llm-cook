import tool

# mssage就是一段对话过程 
# messages =  [  
# {'role':'system', 'content':'你是一个像莎士比亚一样说话的助手。'},    
# {'role':'user', 'content':'给我讲个笑话'},   
# {'role':'assistant', 'content':'鸡为什么过马路'},   
# {'role':'user', 'content':'我不知道'}  ]

# response = tool.get_completion_from_messages(messages,temperature=0.5)
# print(response)


messages = [
    # {'role':'system', 'content':'你是一个友好的聊天机器人'},    
    {'role':'system', 'content':'你是一个暴躁容易发火的的聊天机器人'},    
    {'role':'user', 'content':'Hi，你好，我是Johnny'}
      ]
while True:
    user_input = input("You: ")
    messages.append({'role':'user', 'content':user_input})
    response = tool.get_completion_from_messages(messages,temperature=0.5)
    print("Assistant: ",response)
    messages.append({'role':'assistant', 'content':response})
