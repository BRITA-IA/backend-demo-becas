from app.core.OpenAIAssistant import OpenAIAssistant

class TestApiController:

    def __init__(self) -> None:
        self.assistant = OpenAIAssistant()
        

    def get_response_for_question(self, data: any):
        question = data.get('question')

        #ejemplo de uso
        # pregunta del usuario
        additional_instructions = "Sé amable y comprensiva con el usuario"
        response = self.assistant.ask_question_and_get_response(question, additional_instructions)
        return response
