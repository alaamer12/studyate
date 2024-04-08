from transformers import *

model = PegasusForConditionalGeneration.from_pretrained("tuner007/pegasus_paraphrase")
tokenizer = PegasusTokenizerFast.from_pretrained("tuner007/pegasus_paraphrase")

def get_paraphrased_sentences(model, tokenizer, sentence, num_return_sequences=5, num_beams=5) -> list[str, ...]:
    inputs = tokenizer([sentence], truncation=True, padding="longest", return_tensors="pt")
    outputs = model.generate(
        **inputs,
        num_beams=num_beams,
        num_return_sequences=num_return_sequences,
    )
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)

with open('abbrevations.txt', 'r') as f:
    paraphrased_sentences = []
    line = f.read()
    sentences = get_paraphrased_sentences(model, tokenizer, line.replace('\n', ' '), num_beams=1, num_return_sequences=1)
    paraphrased_sentences.extend(sentences)

print(line.replace('\n', ' '))
with open('paraphrased.txt', 'w') as f:

    for sentence in paraphrased_sentences:
        f.write(sentence + '\n')



