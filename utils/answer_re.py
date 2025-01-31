from typing import List
from pydantic import BaseModel, HttpUrl
import re

def parse_model_output(text: str):
    answer_match = re.search(r"<ans>(.*?)</ans>", text)
    reason_match = re.search(r"<reason>(.*?)</reason>", text)
    url_matches = re.findall(r"<url>(.*?)</url>", text)
    
    answer = answer_match.group(1) if answer_match else None
    reasoning = reason_match.group(1) if reason_match else None
    sources: List[HttpUrl] = [HttpUrl(url) for url in url_matches]
    
    
    answer = int(answer) if re.match(r'^-?\d+$', str(answer)) else None
    return answer, reasoning, sources


# if __name__ == "__main__":
#     # Пример использования
#     # text = """
# # <ans>1</ans>
# # <reason>Сокращение Санкт-Петербургского национального исследовательского университета информационных технологий, механики и оптики - НИУ ИТМО или просто ИТМО.</reason>
# # <url>https://abit.itmo.ru/</url>
# # <url>https://www.itmo.ru/</url>
# # <url>https://ru.wikipedia.org/wiki/Университет_ИТМО</url>
# # """

#     text = """
# <ans>NONE</ans>
# <reason>Серия "Гарри Поттер" - это популярная серия романов английской писательницы Джоан К. Роулинг. Серия состоит из семи книг, каждая из которых описывает один год из жизни главного героя - мальчика-волшебника Гарри Поттера. Первая книга серии называется "Гарри Поттер и Философский камень". Книги доступны на русском языке и пользуются большой популярностью. Их можно приобрести в различных книжных магазинах и онлайн-платформах, а также прочитать в электронном формате. Серия "Гарри Поттер" стала культурным феноменом и привлекла миллионы читателей по всему миру.</reason>
# <url>https://www.labirint.ru/books/424618/</url>
# <url>https://harrypotter.fandom.com/ru/wiki/Гарри_Поттер_(серия_романов)</url>
# <url>https://azbooka.ru/serie/garri-potter</url>
# """

#     parsed_output = parse_model_output(text)
#     print(parsed_output)
