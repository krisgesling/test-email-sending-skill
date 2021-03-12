from mycroft import MycroftSkill, intent_file_handler


class TestEmailSending(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sending.email.test.intent')
    def handle_sending_email_test(self, message):
        self.speak_dialog('sending.email.test')


def create_skill():
    return TestEmailSending()

