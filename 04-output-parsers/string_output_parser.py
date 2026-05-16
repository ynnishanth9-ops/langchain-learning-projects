from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    prompt = ChatPromptTemplate.from_template(
        "Give a short professional summary about {topic}."
    )

    parser = StrOutputParser()

    chain = prompt | model | parser

    result = chain.invoke({
        "topic": "AI workflow automation"
    })

    print("Parsed Output:")
    print(result)


if __name__ == "__main__":
    main()
