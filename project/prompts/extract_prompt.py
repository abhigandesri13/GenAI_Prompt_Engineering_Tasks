from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract:
- Skills
- Experience
- Tools

Do NOT assume anything.

Resume:
{resume}

Give output in JSON.
"""
)