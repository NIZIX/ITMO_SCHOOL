from openai import OpenAI

def get_search_query(question):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="-----------------------OpenRouterKey----------------------------",
    )

    completion = client.chat.completions.create(
      model="google/gemma-2-9b-it:free",
      # model="google/gemini-2.0-flash-thinking-exp:free",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": f"Сформируй поисковой запрос по заданному вопросу. Не отвечай на вопрос. Выведи только текст запроса.\n \
              {question}"
            }
          ]
        }
      ]
    )
    
    return completion.choices[0].message.content.strip().strip('"').strip("'")


if __name__ == "__main__":
    que = "В каком рейтинге (по состоянию на 2021 год) ИТМО впервые вошёл в топ-400 мировых университетов?\n1. ARWU (Shanghai Ranking)\n2. Times Higher Education (THE) World University Rankings\n3. QS World University Rankings\n4. U.S. News & World Report Best Global Universities"
    print(get_search_query(que))
