import os
import json

def extract_process(target_files):
    for target_file in target_files:
        with open('./transcript_data/' +target_file) as f:
            data = json.load(f)

            # 話者の情報が入っている部分
            speaker_list = data['results']['speaker_labels']['segments']
            # 文字起こし部分
            transcribe_list = data['results']['items']

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
                for item in trans_segment['items']:
                    output_txt += item['content']
                output_txt += '\n'

            # ファイルに出力
            file_name = 'timeline_data/' +target_file.split('.')[0] + '.txt'
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(output_txt)
    return 


if __name__ == '__main__':
    target_files = os.listdir('./transcript_data')
    extract_process(target_files)
