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
        speaker_list = data['results']['speaker_labels']['segments']
        count = 0
        # print(len(speaker_list))
        # length = len(speaker_list)
        for i in range(len(speaker_list)-1):
            # print('start_time:' + speaker_list[i]['start_time'] + ' endtime:' + speaker_list[i]['end_time'])
            tmp = float(speaker_list[i]['start_time'])
            if tmp > float(speaker_list[i + 1]['start_time']):
                count += 1
                print(type(tmp))
                print('tmp:' + tmp)
                print('next:' + speaker_list[i + 1]['start_time'])
        
        print(count)

        # print(type(speaker_list))
        # print(speaker_list[0])
        # # listに格納する
        # transcribe_list = data['results']['items']
        # # start_timeの順番にソート
        # transcribe_list.sort(key=lambda x: x['start_time'])
        # # 連続した話者情報をまとめる

        # print(transcribe_list[0])
        # print(transcribe_list[0].update(speaker_list[0]))
        # print(transcribe_list[0])
        # 話者情報と結合
        # for index,item in enumerate(transcribe_list):
        #     item.update(speaker_list[index])
        # print(transcribe_list)
        # # 信頼性が低い要素を削除
        # transcribe_list = [item for item in transcribe_list if float(item['alternatives'][0]['confidence']) > 0.5]

        # print(transcribe_list)
    return 


if __name__ == '__main__':
    target_files = os.listdir('./transcript_data')
    extract_process(target_files)
