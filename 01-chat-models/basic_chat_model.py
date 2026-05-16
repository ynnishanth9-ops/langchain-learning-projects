from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    response = model.invoke("Explain LangChain in simple words.")

    print("AI Response:")
    print(response.content)


if __name__ == "__main__":
    main()
