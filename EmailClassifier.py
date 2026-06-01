import KeyWords
from pymorphy3 import MorphAnalyzer
analyzer = MorphAnalyzer()

class EmailClassifier:
    def __init__(self, email):
        self.email = email

        self.email.edit_from()
        self.email.edit_to()
        self.email.edit_date()
        self.email.edit_subject()
        self.email.edit_attachment()
        self.email.edit_text()

        self.SPAM_STATUS = "spam"

        self.URGENT_STATUS = "urgent"
        self.URGENT_STATUS_NO_ATTACHMENTS = "urgent/no-attachments"
        self.URGENT_STATUS_ATTACHMENTS = "urgent/attachments"

        self.NON_URGENT_STATUS = "non-urgent"
        self.NON_URGENT_STATUS_NO_ATTACHMENTS = "non_urgent/no-attachments"
        self.NON_URGENT_STATUS_ATTACHMENTS = "non_urgent/attachments"

        self.NON_CLASSIFIED_STATUS = "non_classified"

        self.email_text = email.Text if email.Text is not None else []

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
                        return self.classify_attachments(self.URGENT_STATUS)
        return self.classify_attachments(self.NON_URGENT_STATUS)

    def classify_attachments(self, current_status):
        has_attachment = True if self.email.Attachment is not None else False
        if has_attachment:
            if current_status == self.URGENT_STATUS:
                return self.URGENT_STATUS_ATTACHMENTS
            else:
                return self.NON_URGENT_STATUS_ATTACHMENTS
        else:
            if current_status == self.URGENT_STATUS:
                return self.URGENT_STATUS_NO_ATTACHMENTS
            else:
                return self.NON_URGENT_STATUS_NO_ATTACHMENTS

    def classify(self):
        current_status = self.classify_spam()
        if current_status == self.SPAM_STATUS:
            return self.SPAM_STATUS
        else:
            return self.classify_urgent()
