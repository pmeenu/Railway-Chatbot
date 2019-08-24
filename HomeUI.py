
import ChatFns
import argparse
import uuid
import os

class stu_live:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'
        font9 = "-family {Segoe UI} -size 13 -weight bold -slant roman" \
                " -underline 0 -overstrike 0"
        self.top=top
        top.title("Machine Learning Chatbot")
        top.geometry("400x500")
        top.resizable(width=ChatFns.FALSE, height=ChatFns.FALSE)
        top.configure(background="#c0c0c0")
        self.ChatLog = ChatFns.Text(top, bd=0, bg="white", height="8", width="50", font="Arial", )
        self.ChatLog.insert(ChatFns.END, "Connecting to your partner..\n")
        self.ChatLog.config(state=ChatFns.DISABLED)
        scrollbar = ChatFns.Scrollbar(self.top, command=self.ChatLog.yview, cursor="heart")
        self.ChatLog['yscrollcommand'] = scrollbar.set
        self.SendButton = ChatFns.Button(self.top, font=30, text="Send", width="12", height=5,
                                         bd=0, bg="#FFBF00", activebackground="#FACC2E",
                                         command=self.ClickAction)
        self.EntryBox = ChatFns.Text(self.top, bd=0, bg="white", width="29", height="5", font="Arial")
        self.EntryBox.bind("<Return>", self.DisableEntry)
        self.EntryBox.bind("<KeyRelease-Return>", self.PressAction)
        scrollbar.place(x=376, y=6, height=386)
        self.ChatLog.place(x=6, y=6, height=386, width=370)
        self.EntryBox.place(x=128, y=401, height=90, width=265)
        self.SendButton.place(x=6, y=401, height=90)

    def detect_intent_texts(self,project_id, session_id, texts, language_code):
        import dialogflow_v2 as dialogflow
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(project_id, session_id)
        print('Session path: {}\n'.format(session))
        text_input = dialogflow.types.TextInput(
            text=texts, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        ChatFns.LoadOtherEntry(self.ChatLog, format(
            response.query_result.fulfillment_text) +"\n")
        ChatFns.playsound('notif.wav')
        if self.top.focus_get() == None:
            ChatFns.FlashMyWindow("Machine Learning Chatbot")
    def ClickAction(self):
       print("hello")
    def PressAction(self):
        print("hi")
    def ClickAction(self):

        EntryText = ChatFns.FilteredMessage(self.EntryBox.get("0.0", ChatFns.END))
        ChatFns.LoadMyEntry(self.ChatLog, EntryText)
        self.ChatLog.yview(ChatFns.END)
        self.EntryBox.delete("0.0", ChatFns.END)

        self.detect_intent_texts("women-security-system-40-ec", "sessiontest", EntryText, "en");
    def PressAction(self,event):
        self.EntryBox.config(state=ChatFns.NORMAL)
        self.ClickAction()

    def DisableEntry(self,event):
        self.EntryBox.config(state=ChatFns.DISABLED)

def vp_start_gui():
    global val, w, root
    root = ChatFns.Tk()
    top = stu_live(root)
    root.mainloop()

if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key/women-security-system-40-ec-496d98e094a4.json"
    vp_start_gui()