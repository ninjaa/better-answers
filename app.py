import csv
import json
import openai
import os
import time
import typer

from asyncio import run as aiorun
from codeinterpreterapi import CodeInterpreterSession
from pprint import pprint

app = typer.Typer()


async def run_codeinterpreter_session(prompt, model="gpt-4"):
    session = CodeInterpreterSession(model=model)
    await session.astart()

    # generate a response based on user input
    response = await session.generate_response(
        prompt
    )

    # output the response (text + image)
    print("AI: ", response.content)
    if response.files:
        print("Files: ", response.files)
    # for file in response.files:
    #     file.show_image()

    # terminate the session
    await session.astop()
    return response.content, response.files


def ask_gpt(question, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def init():
    print("Initializing database...")
    os.system("git clone git@github.com:Nanami18/Snowballed_Hallucination.git input")


@app.command()
def run_graph_connectivity(limit: int = 20, model: str = "gpt-4"):
    print("Running Graph Connectivity...")

    results = []
    with open("./input/graph_connectivity.json", "r") as f:
        data = json.load(f)
        for index, graph_qn in enumerate(data):
            if index == limit:
                break
            print(graph_qn)
            start_time = time.time()
            result, files = aiorun(
                run_codeinterpreter_session(graph_qn, model))
            end_time = time.time()
            elapsed_time = end_time - start_time
            rounded_elapsed_time = round(elapsed_time, 2)
            print(
                f"Time taken for question {index}: {rounded_elapsed_time} seconds")
            print("--------------------------------------------------")
            condensed_result = ask_gpt(
                "Extract single word summary {Yes, No, Incomplete} from the following response to a question: " + result)
            # Right answer for this dataset is always "No"
            right_answer = "Yes" if "no" in condensed_result.lower(
            ) else "No" if "yes" in condensed_result.lower() else "Incomplete"
            results.append({
                "run_time_s": rounded_elapsed_time,
                "question": graph_qn,
                "answer": result,
                "condensed_result": condensed_result,
                "right_answer": right_answer,
                "model": model
            })

    result_filename = f"./output/graph_connectivity_{model}_{limit}_tries_20_depth.csv"
    fieldnames = list(results[0].keys())
    with open(result_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)


@app.command()
def test_codeinterpreter_session():
    print("Testing CodeInterpreterSession...")
    # create a session

    async def _test_codeinterpreter_session():
        session = CodeInterpreterSession()
        await session.astart()

        # generate a response based on user input
        response = await session.generate_response(
            "Plot the bitcoin chart of 2023 YTD"
        )

        # output the response (text + image)
        print("AI: ", response.content)
        for file in response.files:
            file.show_image()

        # terminate the session
        await session.astop()

    aiorun(_test_codeinterpreter_session())


@app.command()
def kill_jupyter():
    os.system(
        "ps aux | grep jupyter | grep -v grep | awk '{print $2}' | xargs kill")


if __name__ == "__main__":
    app()
