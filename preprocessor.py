import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm
def process_posts(raw_file_path, processsed_file_path=None):
    enriched_post = []
    with open(raw_file_path, encoding='utf-8') as file:
        post = json.load(file)
        for post in post:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_post.append(post_with_metadata)
        
        for epost in enriched_post:
            print(epost)

def extract_metadata(post):
    template = ''

    return {
        'line_count': 10,
        'language': 'English',
        'tags': ['Mental health', 'Motivation']

    }
if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")