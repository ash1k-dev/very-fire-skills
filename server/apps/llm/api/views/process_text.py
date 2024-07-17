from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.llm import LocalProvider
from server.apps.llm.services import get_llm_answer


class TextProcessorView(APIView):
    """Viewset для обработки текста"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Обработка текста"""
        text = request.data.get("text")
        if not text:
            return Response(
                {"error": "Нужно передать текст для исправления ошибок"}, status=400
            )
        corrected_text = self._process_text(text)
        return Response({"text": corrected_text})

    def _process_text(self, text):
        """Запрос к LLM для исправления ошибок"""
        text = get_llm_answer(text=text, provider=LocalProvider())
        return text
