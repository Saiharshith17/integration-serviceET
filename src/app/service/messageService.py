from utils.messageUtil import MessageUtil

class MessageService:
    def __init__(self):
        self.messageUtil=MessageUtil();
        self.llmService=LLMService();