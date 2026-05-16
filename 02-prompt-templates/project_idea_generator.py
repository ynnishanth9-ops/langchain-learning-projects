from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI project mentor helping students build portfolio projects."),
        ("human", """
Suggest 3 beginner-friendly AI automation project ideas for someone learning {technology}.

For each idea, include:
1. Project name
2. Problem solved
3. Main features
4. Suggested tech stack
""")
    ])

    chain = prompt | model

    response = chain.invoke({
        "technology": "LangChain"
    })

    print("Generated Project Ideas:")
    print(response.content)


if __name__ == "__main__":
    main()
