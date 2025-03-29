from langchain.chat_models import ChatOpenAI
from langchain.llms.base import LLM

def load_llm(provider: str, model_name: str, api_key: str) -> LLM:
    provider = provider.lower()

    if provider == "openai":
        return ChatOpenAI(model_name=model_name, temperature=0, openai_api_key=api_key)

    elif provider == "claude":
        from langchain.chat_models import ChatAnthropic
        return ChatAnthropic(model=model_name, temperature=0, anthropic_api_key=api_key)

    elif provider == "huggingface":
        from langchain import HuggingFaceHub
        return HuggingFaceHub(repo_id=model_name, model_kwargs={"temperature": 0}, huggingfacehub_api_token=api_key)

    else:
        raise ValueError(f"不支援的 LLM 提供者：{provider}")
