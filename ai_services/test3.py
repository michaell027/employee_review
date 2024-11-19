import torch
from torch import cuda, bfloat16
print(torch.cuda.is_available())  # Should return True
print(torch.cuda.device_count())  # Should return the number of GPUs


from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM, BitsAndBytesConfig
import transformers

bnb_config = transformers.BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=bfloat16
)

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)

model = AutoModelForCausalLM.from_pretrained(
    model,
    device_map={"": 0},
    quantization_config=bnb_config
)

model.config.use_cache = False
model.config.pretraining_tp = 1

model = model.to("cuda")

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

sequence = pipeline("Hi! Who are you?.", do_sample=True)

print(sequence)