# Code for explainable Fact-checking


import random
from prompt_library import *
from args import *
from src.data.utils import *
from vllm import LLM, SamplingParams
from openai import AzureOpenAI



if args.LLM_model == "llama-2-7b":
    model_path = "Llama-2-7b-chat-hf"
    tokenizer = "hf-internal-testing/llama-tokenizer"
    llm_model = LLM(model_path, tokenizer)

if args.LLM_model == "gpt-4":
    client = AzureOpenAI(
        azure_endpoint="xxx",
        api_key="xxx",
        api_version="2024-02-15-preview"
    )

if args.LLM_model == "finetune_llama-2":
    model_path = "./finetune_model/LoRA_finetune/mixed_4batch"
    tokenizer = "hf-internal-testing/llama-tokenizer"
    llm_model = LLM(model_path, tokenizer)


sampling_params = SamplingParams(temperature=0.2, top_p=0.9, top_k=1, use_beam_search=False, max_tokens=4096, # 256 for closed_domain; 1024 for open_domain
                                     presence_penalty=0.0, frequency_penalty=2)
def LLM_participate(prompt, sampling_params, claim=None, evidence=None):
    full_prompt = prompt.format(claim, evidence)

    if args.LLM_model == "llama-2-7b" or args.LLM_model == "finetune_llama-2":
        result = llm_model.generate(full_prompt, sampling_params)
        output = result[0].outputs[0].text

    elif args.LLM_model == "gpt-4":
        response = client.chat.completions.create(
          model = "deployment_name"
          messages = [{"role": "system", "content": full_prompt}],
          temperature=0.2,
          max_tokens=4096,
          top_p=0.9,
          frequency_penalty=2,
          presence_penalty=0,
          stop=None
        )
        output = response.choices[0].message.content
        # print(output)
    return output

def evidence_correlation(claim, evidence):
    results = []
    if evidence == []:
        return results
    prompt = correlation_degree
    for e in evidence:

        output = LLM_participate(prompt, sampling_params, claim, e)
        result = output
        relationship = result.split('\n')[0].strip()
        results.append(relationship)
    # input(results)
    return results

def fact_verification(claim, evidence, relation=None):
    if relation == None and evidence != []:
        Evidence = ''
        i = 1
        for e in evidence:
            Evidence += 'Evidence ' + str(i) + ': ' + e + '\n'
            i += 1
        print(Evidence)
        prompt = verification_wo_correlation_split


    elif relation != None and relation != [] and evidence != []:
        Evidence = ''
        i = 1
        for e, r in zip(evidence, relation):
            Evidence += 'Evidence ' + str(i) + ': ' + e + ' & ' + 'Correlation ' + str(i) + ': ' + r.split(": ")[-1] + '\n '
            i += 1
        print(Evidence)
        prompt = verification_w_correlation_split

    else:
        output = ['Output: Label: Uncertain.', 'Explanation: No evidence detected.']
        return output

    output = LLM_participate(prompt, sampling_params, claim, Evidence) # verification
    result = output
    check = result.split('\n')[0].strip()
    verdict_exp = check.split('     ')  
    return verdict_exp

def explainable_checking(claim, evidence, index=None):

    if args.setting == "Baseline":
        correlation = None
        verdict_w_explain = fact_verification(claim, evidence)

    elif args.setting == "Automatic":
        correlation = evidence_correlation(claim, evidence)
        verdict_w_explain = fact_verification(claim, evidence, correlation)
        assert len(evidence) == len(correlation)

    elif args.setting == "Input":

        correlation_path = "./output_results/open_Llama2-finetune/automatic_Llama-2_wo.pkl"
        correlation_data = load_pickle(correlation_path)
        correlation = correlation_data[index]["correlation"]

        assert len(evidence) == len(correlation)
        # input(correlation)
        # input(evidence)
        verdict_w_explain = fact_verification(claim, evidence, correlation)

    return correlation, verdict_w_explain

def shuffle_data(data):
    random.shuffle(data)
    return data

if __name__ == "__main__":

    save_path = 'automatic_Llama-2-finetune.pkl'

    if args.claim_domain == "closed":
        dataset = './explanation_annotation/closed_fever/close_fever.json'
        claims = read_json(dataset)
        # input(claims)

        """Explainable Fact-Checking"""
        i = 0
        for c in range(len(claims)):
            i += 1
            evidence = list()
            claim = claims[c]["claim"]
            for e in claims[c]["evidence"]:
                evidence.append(e["sentence"])

            correlation, verdict_w_explain = explainable_checking(claim, evidence, c)

            preds = dict()
            preds["claim"] = claim
            preds["evidence"] = evidence
            preds["correlation"] = correlation
            preds["verdict_w_explain"] = verdict_w_explain
            print(preds)
            save_pickle(save_path, preds)
            results = load_pickle(save_path)
            print(i)
            print(len(results))
            if i != len(results):
                print(claims[i]["claim"])
                break

    if args.claim_domain == "open":
        dataset = './explanation_annotation/open_fever/open_fever.json'
        claims = read_json(dataset)


        """Explainable Fact-Checking"""
        i = 0
        for c in range(0, len(claims)): # 50
            try:
                i += 1
                evidence = list()
                claim = claims[c]["claim"]

                for e in claims[c]["evidence"]:
                    evidence.append(e) 

                correlation, verdict_w_explain = explainable_checking(claim, evidence, c)

                preds = dict()
                preds["claim"] = claim
                preds["evidence"] = evidence
                preds["correlation"] = correlation
                preds["verdict_w_explain"] = verdict_w_explain
            except:
                preds = dict()
                preds["claim"] = claim
                preds["evidence"] = evidence
                preds["correlation"] = []
                preds["verdict_w_explain"] = ""
            print(preds)
            save_pickle(save_path, preds)
            results = load_pickle(save_path)
            print(i)
            print(len(results))
            if i != len(results):
                print(claims[i]["claim"])
                break

    if args.claim_domain == "fever":
        dataset = './explanation_annotation/closed_fever/fever_dataset.json'
        claims = read_json(dataset)


        """Explainable Fact-Checking"""
        i = 0
        for c in range(len(claims)):
            i += 1
            evidence = list()
            claim = claims[c]["claim"]
            for e in claims[c]["evidence"]:
                evidence.append(e["sentence"])

            correlation, verdict_w_explain = explainable_checking(claim, evidence, c)

            preds = dict()
            preds["claim"] = claim
            preds["evidence"] = evidence
            preds["correlation"] = correlation
            preds["verdict_w_explain"] = verdict_w_explain
            print(preds)
            save_pickle(save_path, preds)
            results = load_pickle(save_path)
            print(i)
            print(len(results))
            if i != len(results):
                print(claims[i]["claim"])
                break














