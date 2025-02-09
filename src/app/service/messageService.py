from app.utils.messageUtil import MessageUtil
from app.service.llmService import LLMService

class MessageService:
    def __init__(self):
        self.messageUtil=MessageUtil()
        self.llmService=LLMService()

    def process_message(self,message):
        if self.messageUtil.isBankSms(message):
            expense=self.llmService.runLLM(message)
            return expense if isinstance(expense, dict) else expense.model_dump()
        else:
            return None