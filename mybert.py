import torch
from transformers.tokenization_bert_japanese import BertJapaneseTokenizer
from transformers.modeling_bert import BertForMaskedLM, BertConfig
import MeCab

# Load the models
tokenizer = BertJapaneseTokenizer.from_pretrained('model/')
config = BertConfig.from_json_file('model/bert_base_32k_config.json')
model = BertForMaskedLM.from_pretrained('model/model.ckpt-580000_pytorch.bin', config=config)
m=MeCab.Tagger("-Ochasen")

def sent_emb(text):
    print('text:', text)
    input_ids = tokenizer.encode(text, return_tensors='pt')
    print('tokenizer.conert:', tokenizer.convert_ids_to_tokens(input_ids[0].tolist()))

    masked_index = torch.where(input_ids == tokenizer.mask_token_id)[1].tolist()[0]
    print('masked index:', masked_index)
    result = model(input_ids)
    pred_ids = result[0][:, masked_index].topk(10).indices.tolist()[0]

    output = []
    for pred_id in pred_ids:
        output_ids = input_ids.tolist()[0]
        output_ids[masked_index] = pred_id
        text = ''.join(tokenizer.decode(output_ids))
        #print(text)
        text_segmented = m.parse(text)
        # print(text_segmented)
        sub = []
        for line in text_segmented.split('\n')[3:-5]:
            tmp = line.split('\t')
            print(tmp)
            rslt = {}
            rslt['surface'] = tmp[0]
            rslt['baseform'] = tmp[2]
            rslt['pos'] = tmp[3:6]
            sub.append(rslt)
        output.append(sub)
        print('------')
    return output

