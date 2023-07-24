# Better Answers with GPT-4 Code Interpreter

This repo is published in association with a blog post on medium entitled [Significantly Mitigate GPT-4 Hallucinations using Code Interpeter](https://aditya-advani.medium.com/mitigate-gpt-4-hallucinations-using-code-interpreter-29fea4887eec)

## How to rerun analysis

### Prereqs

- Python 3.11
- Poetry
- OpenAI API key exported to env as OPENAI_API_KEY

### Commands

```bash
poetry install
poetry shell
python app.py init
```

Execution of GPT-4 with Code Interpreter

```bash
python app.py run-graph-connectivity --limit 1 --model gpt-4
```

In order to see the AgentExecutor chain, I'm jumping into the codeinterpreter-api library CodeInterpreterApiSettings and setting Verbose to True.

You can see output of some runs in the output folder.

Please reach out to me on [Twitter](https://twitter.com/aditya_advani) with questions or comments. Very interested in this problem happy to hack on various aspects of it more.


## Very helpful links

- how to use typer commands async https://github.com/tiangolo/typer/issues/88#issuecomment-889530263