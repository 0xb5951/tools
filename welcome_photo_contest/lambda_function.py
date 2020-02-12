import json
import boto3
import os



#画像ダウンロード
def get_image(image_url,token):
    bot_token = os.getenv('SLACK_BOT_USER_ACCESS_TOKEN')
    headers = {'Authorization': 'Bearer {}'.format(bot_token)}

    image = requests.get(image_url,headers=headers)

    return image.content

def get_slack_file(token,file_id):
    bot_token = os.getenv('SLACK_BOT_USER_ACCESS_TOKEN')
    headers = {'Authorization': 'Bearer {}'.format(bot_token)}

    response = requests.get('https://slack.com/api/files.info'+'?file='+file_id,headers=headers)

    return json.loads(response.text)

#Slackに投稿
def Slack_post(webhook_url,label,text,key):
    bot_token = os.getenv('SLACK_BOT_USER_ACCESS_TOKEN')
    message ='S3に'+key+'をアップロードしました。\n'
    message +='解析結果\n'
    message +='\n物体検出\n'

    #物体検出
    for lb_n in label:
        message +=lb_n['Name']+':'+str(round(float(lb_n['Confidence']),1))+'%\n'

    message +='\nテキスト検出\n'

    #テキスト検出
    for tex_n in text:
        message +=tex_n['DetectedText']+':'+str(round(float(tex_n['Confidence']),1))+'%\n'

    item= { 'text':  message }

    headers = {'Content-type': 'application/json'}

    try:
      requests.post(webhook_url,json=item,headers=headers)

    except Exception as e:
      logging.info("type:%s", type(e))
      logging.error(e)

    return

def lambda_handler(event, context):
    bot_token = os.getenv('SLACK_BOT_USER_ACCESS_TOKEN')
    # TODO implement
    print(event)

    # 画像取得？
    file_res = get_slack_file(bot_token, event['event']['file_id'])
    print(file_res)
    if event['event']['text'] in '<@UTHADKVA6>':
        print('check run')

    return {
        'statusCode': 200
    }
