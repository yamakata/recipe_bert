import torch
from transformers.tokenization_bert_japanese import BertJapaneseTokenizer
from transformers.modeling_bert import BertForMaskedLM, BertConfig

# Load the models
tokenizer = BertJapaneseTokenizer.from_pretrained('model/')
config = BertConfig.from_json_file('model/bert_base_32k_config.json')
model = BertForMaskedLM.from_pretrained('model/model.ckpt-580000_pytorch.bin', config=config)


def sent_emb(text):
    print('text:', text)
    input_ids = tokenizer.encode(text, return_tensors='pt')
    print('tokenizer.conert:', tokenizer.convert_ids_to_tokens(input_ids[0].tolist()))

    masked_index = torch.where(input_ids == tokenizer.mask_token_id)[1].tolist()[0]
    print('masked index:', masked_index)
    result = model(input_ids)
    pred_ids = result[0][:, masked_index].topk(10).indices.tolist()[0]

    '''
    output = []
    for pred_id in pred_ids:
        output_ids = input_ids.tolist()[0]
        output_ids[masked_index] = pred_id
        print(tokenizer.decode(output_ids))
        output.append(tokenizer.decode(output_ids))
    return output
    '''
    return tokenizer.decode(pred_ids).split(' ')
