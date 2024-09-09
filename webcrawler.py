from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate

loader = WebBaseLoader("https://jobs.nike.com/job/R-31388")
page_data = loader.load().pop().page_content

print(page_data)

prompt_extract = PromptTemplate.from_template(
    
)