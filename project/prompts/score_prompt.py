from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match"],
    template="""
Give score from 0 to 100.

Match Data:
{match}
"""
)