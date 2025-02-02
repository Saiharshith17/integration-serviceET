import re

class MessageUtil:
    def isBankSms(self,message):
        word_to_search=['spent','card','bank']
        pattern=r'\b(?:' + '|'.join(re.escape(word) for word in word_to_search)+r')\b'
        return bool(re.search(pattern=pattern,message,flags=re.IGNORECASE))
    