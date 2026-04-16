from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "match"],
    template="""
Explain why this score is given.

Score: {score}
Match: {match}
"""
)