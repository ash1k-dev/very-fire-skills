import re

from sentry_sdk import capture_exception

from server.settings.components.llm import DEFAULT_CHUNK_SIZE


def split_text_into_chunks(text, chunk_size=DEFAULT_CHUNK_SIZE):
    """Разделение текста на части по заданной длине"""
    sentences = re.split(r"(?<=[.!?]) +", text)
    chunks = []
    current_chunk = []
    current_chunk_size = 0

    for sentence in sentences:
        if current_chunk_size + len(sentence) > chunk_size:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_chunk_size = len(sentence)
        else:
            current_chunk.append(sentence)
            current_chunk_size += len(sentence)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


class TextProcessingException(BaseException):
    """Исключение для обработки текста"""

    pass


def get_llm_answer(text, provider):
    """Запрос к LLM для исправления ошибок"""
    chunks = split_text_into_chunks(text)
    result = []
    for chunk in chunks:
        try:
            answer = provider.chat(chunk)
            result.append(answer)
        except Exception as e:
            capture_exception(e)
            raise TextProcessingException
    return " ".join(result)
