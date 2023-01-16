import spacy

nlp = spacy.load("en_core_web_sm")


def anonymize_text(sentences):
    doc = nlp(sentences)

    sent_arr = [x for x in sentences]
    ptr = 0
    flag_propn_before = 0
    flag_blank = 0

    for token in doc:
        token_len = len(token.text)
        if token.pos_ == "PROPN":
            # 1. flagp = 1 -> ptr -1 = X
            if flag_propn_before == 1 and flag_blank == 1 :
                sent_arr[ptr-1] = "X" 
            flag_propn_before=1
            for i in range(token_len):
                sent_arr[ptr+i] = "X"
        else:
          flag_propn_before=0
        ptr += token_len

        if ptr is not len(sentences) and sent_arr[ptr] == " ":
            ptr += 1
            flag_blank = 1
        else:
            flag_blank = 0
    return "".join(sent_arr)
