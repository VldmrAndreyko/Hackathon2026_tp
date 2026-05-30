import KeyWords

class Email:
    def __init__(self, message_text):
        self.FullContent = message_text
        self.From = None
        self.To = None
        self.Date = None
        self.Subject = None
        self.Attachment = None
        self.Text = None

    def edit_from(self):
        key_words = KeyWords.KeyWords().get_from_words()
        for string in self.FullContent:
            string_words = string.split()
            for i in range(len(string_words)):
                string_words[i].lower()
                if string_words[i].strip(":").lower() in key_words:
                    if i + 1 < len(string_words):
                        self.From = " ".join(string_words[i + 1:])
                        return True
        return False

    def edit_to(self):
        key_words = KeyWords.KeyWords().get_to_words()
        for string in self.FullContent:
            string_words = string.split()
            for i in range(len(string_words)):
                if string_words[i].strip(":").lower() in key_words:
                    if i + 1 < len(string_words):
                        self.To = " ".join(string_words[i + 1:])
                        return True
        return False

    def edit_date(self):
        key_words = KeyWords.KeyWords().get_date_words()
        for string in self.FullContent:
            string_words = string.split()
            for i in range(len(string_words)):
                if string_words[i].strip(":").lower() in key_words:
                    if i + 1 < len(string_words):
                        self.Date = " ".join(string_words[i + 1:])
                        return True
        return False

    def edit_subject(self):
        key_words = KeyWords.KeyWords().get_subject_words()
        for string in self.FullContent:
            string_words = string.split()
            for i in range(len(string_words)):
                if string_words[i].strip(":").lower() in key_words:
                    if i + 1 < len(string_words):
                        self.Subject = " ".join(string_words[i + 1:])
                        return True
        return False

    def edit_attachment(self):
        key_words = KeyWords.KeyWords().get_attachment_words()
        for string in self.FullContent:
            string_words = string.split()
            for i in range(len(string_words)):
                if string_words[i].strip(":").lower() in key_words:
                    if i + 1 < len(string_words):
                        self.Attachment = " ".join(string_words[i + 1:])
                        return True
        return False

    def edit_text(self):
        key_words = (KeyWords.KeyWords().get_from_words() + KeyWords.KeyWords().get_to_words() +
                     KeyWords.KeyWords().get_date_words() + KeyWords.KeyWords().get_subject_words() +
                     KeyWords.KeyWords().get_attachment_words())
        correct_text = []
        for string in self.FullContent:
            string_words = string.split()
            for i in range(len(string_words)):
                if string_words[i].strip(":").lower() in key_words:
                    break
            else:
                correct_text.append(string)
        if correct_text:
            self.Text = correct_text
            return True
        else:
            return False
