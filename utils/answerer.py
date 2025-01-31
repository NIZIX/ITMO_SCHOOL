from openai import OpenAI
import json

# Global client initialization
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="-----------------------OpenRouterKey----------------------------",
)

def get_answer(parser_output, org_question):
    try:
        # Create chat completion with specified model
        completion = client.chat.completions.create(
            model="meta-llama/llama-3.1-70b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": ''.join([
                        "Ты помощник по анализу документов.\n",
                        "Твоя задача — проверить ответ на вопрос, используя предоставленные документы.\n",
                        "Если вопрос не содержит варианты ответа пронумерованные цифрами от 1 до 10, выведи `NONE` в `<ans>`, но ты все еще должен ответить на этот вопрос в `<reason>`\n",
                        "Если ответ корректный, выведи номер ответа в поле `<ans>`, развернутый ответ (может помочь 'answer-to-check') в поле `<reason>`, ",
                        "а также 3 лучших URL в поля `<url>`\n",
                        "Строго соблюдай формат вывода:\n",
                        "<ans>[номер ответа]</ans>\n",
                        "<reason>[отредактированный ответ]</reason>\n",
                        "<url>[первый лучший URL]</url>\n",
                        "<url>[второй лучший URL]</url>\n",
                        "<url>[третий лучший URL]</url>\n",
                        f"Вопрос: {org_question}\n{parser_output}"
                    ])
                }
            ]
        )
        
        return completion.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"Error occurred while getting completion: {str(e)}")
        return "Error: Failed to get response from API"

# if __name__ == "__main__":
#     # Читаем JSON-файл с тестовыми данными
#     with open("test.json", "r", encoding="utf-8") as f:
#         json_str = f.read()  # Read as string first
#         test_input = str(json.loads(json_str))  # Parse JSON into dictionary
#         # Convert back to formatted string for LLM

#     # print(str(test_input))

#     question = "Какое сокращение получил Санкт-Петербургский национальный исследовательский университет информационных технологий, механики и оптики?\n1. ИТМО\n2. МГИМО\n3. ИТПИ\n4. ИСИТ"

#     print(get_answer(test_input, question))
