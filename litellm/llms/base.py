## This is a template base class to be used for adding new LLM providers via API calls
import litellm 
import httpx, certifi, ssl
from typing import Optional

class BaseLLM:
    _client_session: Optional[httpx.Client] = None
    def create_client_session(self):
        return litellm.client_session if litellm.client_session else httpx.Client()
    
    def create_aclient_session(self):
        return (
            litellm.aclient_session
            if litellm.aclient_session
            else httpx.AsyncClient()
        )
    
    def __exit__(self):
        if hasattr(self, '_client_session'):
            self._client_session.close()
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, '_aclient_session'):
            await self._aclient_session.aclose()

    def validate_environment(self):  # set up the environment required to run the model
        pass

    def completion(
        self,
        *args, 
        **kwargs
    ):  # logic for parsing in - calling - parsing out model completion calls
        pass

    def embedding(
        self,
        *args, 
        **kwargs
    ):  # logic for parsing in - calling - parsing out model embedding calls
        pass
