import json
from tavily import TavilyClient

def parse(query):
    client = TavilyClient(api_key="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")
    
    search_output = client.search(query, 
                                      include_answer="advanced", 
                                      include_raw_content=False, 
                                      max_results=5)
    
    new_results = []
    for result in search_output["results"]:
        new_results.append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"]
        })

    response = {
        "answer-to-check": search_output["answer"],
        "results": new_results
    }
    
    return response

# def main():
#     query = "сокращение Санкт-Петербургского национального исследовательского университета информационных технологий, механики и оптики"
#     result = parse(query)
#     print(result)
    
#     with open('test.json', 'w', encoding='utf-8') as f:
#         json.dump(result, f, ensure_ascii=False, indent=4)

# if __name__ == "__main__":
#     main()
