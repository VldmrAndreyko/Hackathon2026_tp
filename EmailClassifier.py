import KeyWords
from pymorphy3 import MorphAnalyzer
analyzer = MorphAnalyzer()

class EmailClassifier:
    def __init__(self, email):
        self.email = email
        self.SPAM_STATUS = "spam"
        self.URGENT_STATUS = "urgent"
        self.NON_URGENT_STATUS = "non-urgent"
        self.NON_CLASSIFIED_STATUS = "non-classified"
        self.email_text = email.Text

    def classify_spam(self):
        key_words = KeyWords.KeyWords().get_spam_words()
        for string in self.email_text:
            for word in string.split():
                if key_words[0] in word:
                    return self.SPAM_STATUS
                base_word = analyzer.parse(word)[0].normal_form.strip(""":;.,!?/'" """)
                for i in range(1, len(key_words)):
                    key_word_based = analyzer.parse(key_words[i])[0].normal_form
                    if base_word == key_word_based:
                        return self.SPAM_STATUS
        return self.NON_CLASSIFIED_STATUS

    def classify_urgent(self):
        key_words = KeyWords.KeyWords().get_urgent_words()
        for string in self.email_text:
            for word in string.split():
                base_word = analyzer.parse(word)[0].normal_form.strip(""":;.,!?/'" """)
                for i in range(len(key_words)):
                    key_word_based = analyzer.parse(key_words[i])[0].normal_form
                    if base_word == key_word_based:
                        return self.URGENT_STATUS
        return self.NON_URGENT_STATUS

    def classify(self):
        current_status = self.classify_spam()
        if current_status == self.SPAM_STATUS:
            return self.SPAM_STATUS
        else:
            return self.classify_urgent()
