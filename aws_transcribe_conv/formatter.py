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
        # 文字起こし部分
        transcribe_list = data['results']['items']
        print(transcribe_list[0]['start_time'])
        # transcribe_list.sort(key=lambda x: x['start_time'])

        # for segment in transcribe_list:
        #     if 'start_time' in segment:
        #         ''
        #     else: 
        #         print(segment)

        # 話者ごとにまとめた文字起こしデータ
        trans_segments = []
        tran_index = 0
        print(transcribe_list[0])
        for index, segment in enumerate(speaker_list):
            # start_item
            start_segment = segment['items'][0]
            end_segment = segment['items'][-1]
            # print(segment['start_time'])
            # print(start_segment)
            # print(segment['end_time'])
            # print(end_segment)

            tmp_list = []
            while 1:
                tmp_list += transcribe_list[tran_index]['alternatives']
                try:
                    if end_segment['start_time'] == transcribe_list[tran_index]['start_time'] and \
                        end_segment['end_time'] == transcribe_list[tran_index]['end_time']:
                        tran_index += 1
                        break
                except KeyError:
                    ''
                tran_index += 1
                



            # 最後にまとめて格納
            trans_segments += [{'speaker_label': segment['speaker_label'],'items': tmp_list}]

        print(trans_segments[0:5])

            # tmp = float(speaker_list[i]['start_time'])
            # if tmp > float(speaker_list[i + 1]['start_time']):
            #     count += 1
            #     print(type(tmp))
            #     print('tmp:' + tmp)
            #     print('next:' + speaker_list[i + 1]['start_time'])

        # # 開始のセグメント
        # data['results']['speaker_labels']['segments'][i][0]
        # # 終わりのセグメント
        # data['results']['speaker_labels']['segments'][i][-1]

        
        # print(count)

        # print(type(speaker_list))
        # print(speaker_list[0])

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
