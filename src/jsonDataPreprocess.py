import config
import numpy as np
import pandas as pd
import os
import json
import nltk


def load_data_files(json_files):
    for dirname, _, filenames in os.walk(json_files):
        allData = []
        for filename in filenames:
            data_file = open(dirname + filename)
            allData.append(data_file)
            print(os.path.join(dirname, filename))
            return allData

if __name__ == '__main__':

    #allData = load_data_files(JSON_FILE)
    #df = pd.read_json(r'input/datafile.json')
    #export_csv = df.to_csv(r'input/dataset.csv', index=None, header=True)
    count = 0
    sentence = ["Sentence #"]
    word = ["Word"]
    pos = ["POS"]
    tag = ["Tag"]
    df = json.load(open("input/datafile.json"))
    for key,val in df.items():
        for dataVal in val:
            # print(dataVal['data'])
            count=count+1
            for tValues in dataVal['data']:
                sentence.append("Sentence: "+str(count))
                if tValues['text'] is None:
                    word.append('O')
                else:
                    word.append(str(tValues['text']))
                    #pos.append(nltk.pos_tag(tValues['text'].strip()))
                    if count%2 == 0:
                        pos.append("NN")
                    else:
                        pos.append("NNP")
                try:
                    tag.append(str(tValues['entity']))
                except:
                    tag.append('O')

    df = pd.DataFrame({'Sentence #': sentence, 'Word': word, 'POS': pos, 'Tag': tag})
    export_csv = df.to_csv(r'input/dataset.csv', index=None, header=False)

    for i in range(len(word)):
        print(word[i],pos[i],tag[i])









