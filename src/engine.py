from http import HTTPStatus
from protocol import *
from fastapi import Request

from responses import mock_completions_response, mock_chat_completions_response

class MockEngine:
    model: str
    
    def __init__(self, args):
        self.model = args.served_model_name
    
    async def show_available_models(self) -> ModelList:
        """Show available models. Right now we only have one model."""
        model_cards = [
            ModelCard(id=self.model,
                      root=self.model,
                      permission=[ModelPermission()])
        ]
        return ModelList(data=model_cards)

    async def create_chat_completion(self, request: ChatCompletionRequest, raw_request: Request) -> ChatCompletionResponse:
        return mock_chat_completions_response  
    
    async def create_completion(self, request: CompletionRequest, raw_request: Request) -> CompletionResponse:
        return mock_completions_response

    def create_error_response(
            self,
            message: str,
            err_type: str = "BadRequestError",
            status_code: HTTPStatus = HTTPStatus.BAD_REQUEST) -> ErrorResponse:
        return ErrorResponse(message=message,
                             type=err_type,
                             code=status_code.value)

    