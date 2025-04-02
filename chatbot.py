from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class TherapistChatbot:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained('therapy-gpt')
        self.tokenizer = GPT2Tokenizer.from_pretrained('therapy-gpt')
        self.emotion_analyzer = self.load_emotion_analyzer()
        
    async def generate_response(self, user_input):
        emotion = self.analyze_emotion(user_input)
        context = self.build_context(emotion)
        response = self.generate_therapy_response(context, user_input)
        return self.format_response(response)