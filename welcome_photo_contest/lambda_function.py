import json
import boto3
import os
import requests

#画像ダウンロード
def get_image(image_url,bot_token):
    headers = {'Authorization': 'Bearer {}'.format(bot_token)}

    image = requests.get(image_url,headers=headers)

    return image.content

def get_slack_file(token,file_id):
    bot_token = os.environ["SLACK_BOT_USER_ACCESS_TOKEN"]

    response = requests.get('https://slack.com/api/files.info?token='+bot_token+'&file='+file_id)

    return json.loads(response.text)

#Slackに投稿
def post_slack(user, score):
    webhook_url = 'https://hooks.slack.com/services/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'
    bot_token = os.environ["SLACK_BOT_USER_ACCESS_TOKEN"]
    message ='<@{0}>\nこの写真の点数は{1}点です！！'.format(user, score)

    item= { 'text':  message }

    headers = {'Content-type': 'application/json'}
    requests.post(webhook_url,json=item,headers=headers)
    return

def lambda_handler(event, context):
    bot_token = os.getenv('SLACK_BOT_USER_ACCESS_TOKEN')
    # TODO implement
    print(event)

    if event['event']['text'] not in '<@UTHADKVA6>':
        return 0

    file_id = event['event']['files'][0]['id']
    # 画像情報
    file_res = get_slack_file(bot_token, file_id)
    # 画像取得
    byte_image = get_image(event['event']['files'][0]['url_private'], bot_token)
    # Rekognitionのラベル検出を呼び出す。
    rekognition = boto3.client('rekognition', 'ap-northeast-1')
    response = rekognition.detect_faces(Image={'Bytes': byte_image}, Attributes=['ALL'])
    
    face_details = response['FaceDetails']

    sum_smile = 0
    sum_happy = 0
    face_pos = 0
    photo_score = 1000
    human_count = 0
 
    for item in face_details:
        smile = item['Smile']
        emotions = item['Emotions']
        lamdmarks = item['Landmarks']
        human_count += 1

        if smile['Value'] == 'true':
            sum_smile += smile['Confidence'] * 20

        for emotion in emotions:
            if emotion['Type'] == "HAPPY":
                sum_happy += emotion['Confidence'] * 10
        
        for lamdmark in lamdmarks:
            if lamdmark['Type'] == "nose":
                nose_x = abs(lamdmark['X'] - 0.5)*100
                nose_y = abs(lamdmark['Y'] - 0.5)*100
                face_pos += nose_x + nose_y
    
    face_pos /= human_count
    photo_score -= face_pos*10
    photo_score += sum_smile

    post_slack(event['event']['user'], photo_score)

    return 0
