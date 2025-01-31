from typing import List, Tuple, Optional

from utils.search_query import get_search_query
from utils.parser import parse
from utils.answerer import get_answer
from utils.answer_re import parse_model_output
from pydantic import HttpUrl

def pipeline_search(question: str) -> Tuple[Optional[int], Optional[str], List[HttpUrl]]:
    """
    Asynchronous pipeline for search and answer generation
    
    :param question: Input question to process
    :return: Tuple of (answer, reasoning, sources)
    """
    try:
        # Perform search and parsing
        search_query = get_search_query(question)
        parser_output = parse(search_query)
        
        # Get the answer from the model
        llm_response = get_answer(parser_output, question)
        
        answer, reasoning, sources = parse_model_output(llm_response)
        # print(answer, reasoning, sources)
        
        return answer, reasoning, sources
    
    except Exception as e:
        print(f"Error in pipeline search: {e}")
        return None, None, []

# def main():
#     question = "Гарри Поттер"
#     result = pipeline_search(question)
#     print(result)

# if __name__ == '__main__':
#     main()