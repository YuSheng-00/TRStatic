

PROMPT_TEMPLATE = [
{
    "prompt_input": (
        "Below is an instruction that describes a task, paired with an input that provides further context. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
},
{
    "prompt_input": (
        "You are supposed to follow an instruction, and then the input to generate proper response.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "You are supposed to follow an instruction to generate proper response."
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
},
{
    "prompt_input": (
        "Please follow the instruction and input to give a response.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "Please follow the instruction to give a response."
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
},
{
    "prompt_input": (
        "You are an expert, please listen to human instruction and input to generate the response.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "You are an expert, please listen to human instruction to generate the response.\n\n"
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
},
{
    "prompt_input": (
        "Let's follow the instruction to respond to an input.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "Let's follow the instruction to generate a response.\n\n"
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
},
{
    "prompt_input": (
        "The instruction is a description of the task. You need to follow that and respond to the paired input.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "The instruction is a description of the task. You need to follow that and respond.\n\n"
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
},
{
    "prompt_input": (
        "Below is an instruction that describes a task, paired with an input that provides further context. "
        "Write a response that appropriately completes the request.\n\n"
        "Instruction:\n{instruction}\n\nInput:\n{input}\n\nResponse:"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request.\n\n"
        "Instruction:\n{instruction}\n\nResponse:"
    ),
},
{
    "prompt_input": (
        "You are supposed to follow an instruction, and then the input to generate proper response.\n\n"
        "#Instruction:\n{instruction}\n\nInput:\n{input}\n\nResponse:"
    ),
    "prompt_no_input": (
        "You are supposed to follow an instruction to generate proper response."
        "Instruction:\n{instruction}\n\nResponse:"
    ),
},
{
    "prompt_input": (
        "Please follow the instruction and input to give a response.\n\n"
        "Instruction:\n{instruction}\n\nInput:\n{input}\n\nResponse:"
    ),
    "prompt_no_input": (
        "Please follow the instruction to give a response."
        "Instruction:\n{instruction}\n\nResponse:"
    ),
},
{
    "prompt_input": (
        "You are an expert, please listen to human instruction and input to generate the response.\n\n"
        "Instruction:\n{instruction}\n\nInput:\n{input}\n\nResponse:"
    ),
    "prompt_no_input": (
        "You are an expert, please listen to human instruction to generate the response.\n\n"
        "Instruction:\n{instruction}\n\nResponse:"
    ),
},
{
    "prompt_input": (
        "Let's follow the instruction to respond to an input.\n\n"
        "Instruction:\n{instruction}\n\nInput:\n{input}\n\nResponse:"
    ),
    "prompt_no_input": (
        "Let's follow the instruction to generate a response.\n\n"
        "Instruction:\n{instruction}\n\nResponse:"
    ),
},
{
    "prompt_input": (
        "The instruction is a description of the task. You need to follow that and respond to the paired input.\n\n"
        "Instruction:\n{instruction}\n\nInput:\n{input}\n\nResponse:"
    ),
    "prompt_no_input": (
        "The instruction is a description of the task. You need to follow that and respond.\n\n"
        "Instruction:\n{instruction}\n\nResponse:"
    ),
},
]





# system_context = "You are a mathematical expert now. Please try best to think meticulously of the mathematical knowledge and generate response that meet the mathematical constraints"

system_prefix = "<|start_header_id|>system<|end_header_id|>\n\n{system_context}<|eot_id|>"

qa = '<|start_header_id|>user<|end_header_id|>\n\n{query}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'



system_context = "You are a mathematical expert now. You will be given a mathematical problem, analyse the question meticulously, tell me the math concepts and formulas used to solve the problem and give me a step-by-step solution corresponding to the math knowledges"


LLAMA3_PROMPT_TEMPLATE = {
        "prompt_input": (
        "<|start_header_id|>system<|end_header_id|>\n\n{system}<|eot_id|>\n\n"
        "<|start_header_id|>user<|end_header_id|>\n\n### Question:\n{input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
        #"### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (""
        "<|start_header_id|>system<|end_header_id|>\n\n{system}<|eot_id|>\n\n"
        "<|start_header_id|>user<|end_header_id|>\n\n{instruction}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
        #"Write a response that appropriately completes the request.\n\n"
        #"### Instruction:\n{input}\n\n### Response:"
    ),
}

PROMPT_TEMPLATE_SINGLE = {
    "prompt_input": (
        "Below is an instruction that describes a task, paired with an input that provides further context. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
}



system = 'You are a helpful mathematical assistant now.'
MY_PROMPT_SINGLE = {

    "prompt_input": (
        "<|start_header_id|>system<|end_header_id|>\n\nYou are a helpful mathematical assistant now.<|eot_id|>\n\n"
        "<|start_header_id|>user<|end_header_id|>\n\nThink carefully, recall the formulas used to solve the given mathematical problem and give a step-by-step solution.\n\n### Question:\n{question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    ),

    "prompt_no_input": (
        "<|start_header_id|>system<|end_header_id|>\n\nYou are a helpful mathematical assistant now.<|eot_id|>\n\n"
        "<|start_header_id|>user<|end_header_id|>\n\nThink carefully, recall the formulas used to solve the given mathematical problem and give a step-by-step solution.\n\n### Question:\n{question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    )

}