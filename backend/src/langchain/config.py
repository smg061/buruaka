
from src.models import ORJSONModel
from src.config import settings
class LangChainConfig(ORJSONModel):
    BaseUrl: str = "https://api.openai.com/v1/engines/davinci/completions"
    ApiKey: str 
    
    class Config:
        from_attributes = True
        
langchain_config = LangChainConfig(ApiKey=settings.OPENAI_API_KEY)