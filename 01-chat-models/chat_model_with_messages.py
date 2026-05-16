from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

    messages = [
        SystemMessage(content="You are a helpful AI tutor for beginners."),
        HumanMessage(content="What is the difference between LangChain and LangGraph?")
    ]

    response = model.invoke(messages)

    print("AI Response:")
    print(response.content)


if __name__ == "__main__":
    main()
