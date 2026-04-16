from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job"],
    template="""
Compare resume with job description.

Return:
- matched skills
- missing skills

Resume Data:
{resume_data}

Job Description:
{job}
"""
)