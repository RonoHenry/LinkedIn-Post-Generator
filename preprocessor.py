import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def process_posts(raw_file_path, processed_file_path=None):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = {**post, **metadata}  # Dictionary merging
            enriched_posts.append(post_with_metadata)

    for epost in enriched_posts:
        print(epost)

def extract_metadata(post):
    template = """
    You are given a LinkedIn post. You need to extract the number of lines, language of the post, and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language, and tags.
    3. Tags is an array of text tags. Extract a maximum of two tags.
    4. Language should be English or Swahili.

    Here is the actual post on which you need to perform this task:
    {post}
    """
    pt = PromptTemplate.from_template(template)
    chain = llm | pt
    result = chain.invoke({'post': post})  # Pass the post text
    return result  # Assuming the LLM output is in the correct format

if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
