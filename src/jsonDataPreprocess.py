import config
import numpy as np
import pandas as pd
import os
import json
import nltk


def load_data_files(json_files):
    allData = []
    for dirname, _, filenames in os.walk(json_files):

        for filename in filenames:
            # data_file = open(dirname + filename)
            # allData.append(json.load(data_file))
            allData.append(os.path.join(dirname, filename))
            #print(os.path.join(dirname, filename))
    return allData

if __name__ == '__main__':

    allData = load_data_files(config.JSON_FILE)
    #print(allData)
    #df = pd.read_json(r'input/datafile.json')
    #export_csv = df.to_csv(r'input/dataset.csv', index=None, header=True)
    count = 0
    sentence = ["Sentence #"]
    word = ["Word"]
    pos = ["POS"]
    tag = ["Tag"]
    #df = json.load(open("input/datafile.json"))

    for filename in allData:
        #print("FileName:",filename)
        df = json.load(open(filename))
        sentence_,word_,pos_,tag_ = [],[],[],[]
        for key,val in df.items():
            for dataVal in val:
                print(dataVal['data'])
                count=count+1
                for tValues in dataVal['data']:
                    sentence_.append("Sentence: "+str(count))
                    if tValues['text'] is None:
                        word_.append('O')
                    else:
                        word_.append(str(tValues['text']))
                        #pos.append(nltk.pos_tag(tValues['text'].strip()))
                        if count%2 == 0:
                            pos_.append("NN")
                        else:
                            pos_.append("NNP")
                    try:
                        tag_.append(str(tValues['entity']))
                    except:
                        tag_.append('O')
        sentence.extend(sentence_)
        word.extend(word_)
        pos.extend(pos_)
        tag.extend(tag_)
    result_df = pd.DataFrame({'Sentence #': sentence, 'Word': word, 'POS': pos, 'Tag': tag})
    export_csv = result_df.to_csv(r'input/dataset.csv', index=None, header=False)
    """
    for i in range(len(word)):
        print(word[i],pos[i],tag[i])
    """









