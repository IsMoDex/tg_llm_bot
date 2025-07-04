from openai import (
    OpenAI,
    OpenAIError,
    APIConnectionError,
    AuthenticationError,
    RateLimitError,
    BadRequestError,
    InternalServerError,
)
from config import (
    OPENROUTER_API_KEY,
    OPENROUTER_SITE_URL,
    OPENROUTER_SITE_NAME,
    OPENROUTER_MODEL,
)
from utils.logger import logger
from utils.responses import get_response

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

async def get_llm_response(messages: list[dict]) -> str:
    try:
        logger.debug(f"Запрос к LLM: model={OPENROUTER_MODEL}, messages={messages}")

        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=messages,
            extra_headers={
                "HTTP-Referer": OPENROUTER_SITE_URL,
                "X-Title":    OPENROUTER_SITE_NAME,
            },
            extra_body={}
        )

        content = response.choices[0].message.content.strip()
        logger.info("Ответ от LLM успешно получен.")
        return content

    except InternalServerError as e:
        logger.error(f"InternalServerError: {e}", exc_info=True)
        return get_response("or_internal_server_error")

    except RateLimitError as e:
        logger.warning(f"RateLimitError: {e}", exc_info=True)
        return get_response("or_rate_limit_error")

    except AuthenticationError as e:
        logger.error(f"AuthenticationError: {e}", exc_info=True)
        return get_response("or_authentication_error")

    except BadRequestError as e:
        logger.error(f"BadRequestError: {e}", exc_info=True)
        return get_response("or_bad_request_error").format(error=e)

    except APIConnectionError as e:
        logger.error(f"APIConnectionError: {e}", exc_info=True)
        return get_response("or_api_connection_error")

    except OpenAIError as e:
        logger.error(f"OpenAIError: {e}", exc_info=True)
        return get_response("or_llm_api_error").format(error=e)

    except Exception as e:
        logger.critical(f"Непредвиденная ошибка: {e}", exc_info=True)
        return get_response("or_unexpected_error").format(error=e)


########################

# import httpx
# from utils.logger import logger
# from utils.responses import get_response
#
# async def get_llm_response(messages: list[dict]) -> str:
#     try:
#         payload = {
#             "model":       "google/gemma-3-1b",
#             "messages":    messages,
#             "temperature": 0.7,
#             "max_tokens": -1,
#             "stream":      False
#         }
#
#         logger.debug(f"📤 Отправка запроса к LLM: {payload}")
#
#         async with httpx.AsyncClient() as client:
#             response = await client.post(
#                 "http://localhost:1234/v1/chat/completions",
#                 json=payload,
#                 headers={"Content-Type": "application/json"}
#             )
#             response.raise_for_status()
#             data = response.json()
#
#         content = data["choices"][0]["message"]["content"].strip()
#         logger.debug(f"📥 Ответ от LLM: {content}")
#         return content
#
#     except Exception as e:
#         logger.exception("Ошибка при запросе к локальной модели")
#         return get_response("http_local_model_error").format(error=e)
