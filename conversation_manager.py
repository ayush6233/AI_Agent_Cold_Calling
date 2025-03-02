class ConversationManager:
    def __init__(self, scenario):
        self.scenario = scenario
        self.messages = []
        self.state = {}

    def add_message(self, sender, message):
        self.messages.append((sender, message))

    def update_state(self, key, value):
        self.state[key] = value

    def get_conversation_context(self):
        return " ".join(msg for _, msg in self.messages)

    def save_conversation(self):
        pass  # For simplicity, we're not persisting the conversation in this version.
