# Mock responses to send via API

from protocol import ErrorResponse, CompletionResponse, ChatCompletionResponse
import os

MODEL = os.getenv("MODEL", "mock_llm_name")

mock_error_response = ErrorResponse(
    message="Mock error message",
    type="MockError",
    code=400
)

completions_content = {
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": MODEL,
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [
    {
      "text": "\n\nThis is indeed a test",
      "index": 0,
      "logprobs": None,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 7,
    "total_tokens": 12
  }
}

mock_completions_response = CompletionResponse(**completions_content)


chat_completion_content = {
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": MODEL,
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nHello there, how may I assist you today?",
    },
    "logprobs": None,
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}

mock_chat_completions_response = ChatCompletionResponse(**chat_completion_content)