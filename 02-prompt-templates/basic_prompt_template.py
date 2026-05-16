from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        ("human", "Explain {topic} in simple words for a beginner.")
    ])

    chain = prompt | model

    response = chain.invoke({
        "topic": "LangChain prompt templates"
    })

    print("AI Response:")
    print(response.content)


if __name__ == "__main__":
    main()
