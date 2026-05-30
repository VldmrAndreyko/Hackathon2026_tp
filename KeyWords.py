class KeyWords:
    SPAM_KEY_WORDS = ["http", "выиграть", "выигрыш", "скидка", "розыгрыш", "приз"]
    URGENT_KEY_WORDS = ["срочно", "экстренно", "быстро"]

    FROM_KEY_WORDS = ["from", "от кого"]
    TO_KEY_WORDS = ["to", "кому"]
    DATE_KEY_WORDS = ["date", "дата"]
    SUBJECT_KEY_WORDS = ["subject", "тема"]
    ATTACHMENT_KEY_WORDS = ["во вложении", "файл", "прикрепил", "вложение"]

    def get_spam_words(self):
        return self.SPAM_KEY_WORDS.copy()

    def get_urgent_words(self):
        return self.URGENT_KEY_WORDS.copy()

    def get_from_words(self):
        return self.FROM_KEY_WORDS.copy()

    def get_to_words(self):
        return self.TO_KEY_WORDS.copy()

    def get_date_words(self):
        return self.DATE_KEY_WORDS.copy()

    def get_subject_words(self):
        return self.SUBJECT_KEY_WORDS.copy()

    def get_attachment_words(self):
        return self.ATTACHMENT_KEY_WORDS.copy()