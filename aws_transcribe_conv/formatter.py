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
        # print(transcribe_list[0]['start_time'])
        # transcribe_list.sort(key=lambda x: x['start_time'])

        # for segment in transcribe_list:
        #     if 'start_time' in segment:
        #         ''
        #     else: 
        #         print(segment)

        # 話者ごとにまとめた文字起こしデータ
        trans_segments = []
        tran_index = 0

        # 話者データと文字起こしをくっつける
        for index, segment in enumerate(speaker_list):
            start_segment = segment['items'][0]
            end_segment = segment['items'][-1]

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

        output_txt = ''
        # タイムライン形式に変換
        for trans_segment in trans_segments:
            output_txt += trans_segment['speaker_label'] + ' :'
            print(trans_segment)
            for item in trans_segment['items']:
                output_txt += item['content']
            output_txt += '\n'

        print(output_txt)
    return 


if __name__ == '__main__':
    target_files = os.listdir('./transcript_data')
    extract_process(target_files)
