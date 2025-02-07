from utils.messageUtil import MessageUtil
from service.llmService import LLMService

class MessageService:
    def __init__(self):
        self.messageUtil=MessageUtil()
        self.llmService=LLMService()

    def process_message(self,message):
        if self.messageUtil.isBankSms(message):
            expense=self.llmService.runLLM(message)
            return expense.dict()
        else:
            return None