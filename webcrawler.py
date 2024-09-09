from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from utils import *

loader = WebBaseLoader("https://jobs.nike.com/job/R-31388")
page_data = loader.load().pop().page_content

prompt_extract = PromptTemplate.from_template(
    """
    ### SCRAPED TEXT FROM  WEBSITE:
    {page_data}
    ### INSTRUCTION:
    The Scraped text is from the career's page of a website.
    Your job is to extract the job postings and return them in JSON format containing following keys: 'role', 'experience', 'skills', and 'description'.
    Only return the valid JSON.
    ### VALID JSON (NO PREAMBLE)
    """
)

chain_extract  = prompt_extract | llm
result = chain_extract.invoke(input = {'page_data': page_data})

json_parser = JsonOutputParser()
json_result = json_parser.parse(result.content)

print(json_result)