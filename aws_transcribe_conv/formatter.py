import os
import json

def conv_color(confidence: float) -> str:
    if confidence == 1:
        return "black"
    elif confidence >= 0.9:
        return "gray"
    else:
        return "silver"

    # for item in :
    #     confidence = float(item['alternatives'][0]['confidence'])

    #     print(f'<font color="{color}">', end='')
    #     print(item['alternatives'][0]['content'], end='')
    #     print('</font>', end='')

def extract_process(target_files):
    with open('./transcript_data/' +target_files[0]) as f:
        data = json.load(f)

        # 話者の情報が入っている部分
        speaker_list = data['results']['speaker_labels']

        # listに格納する
        transcribe_list = data['results']['items']
        # 話者情報と結合

        # 信頼性が低い要素を削除
        transcribe_list = [item for item in transcribe_list if float(item['alternatives'][0]['confidence']) > 0.5]
        # start_timeの順番にソート
        transcribe_list.sort(key=lambda x: x['start_time'])
        print(transcribe_list)
    return 


if __name__ == '__main__':
    target_files = os.listdir('./transcript_data')
    extract_process(target_files)
