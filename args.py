import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--LLM_model",
    type=str,
    default="finetune_llama-2",
    help="Specify LLM model [llama-2-7b, gpt-4, finetune_llama-2]",
)

parser.add_argument(
    "--claim_domain",
    type=str,
    default="closed",
    help="Fact checking scenario [closed, open, fever]",
)

parser.add_argument(
    "--setting",
    type=str,
    default="Automatic",
    help="Settings [Baseline, Input, Automatic]",
)


args = parser.parse_args()

print(args)
