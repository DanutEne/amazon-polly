import boto3

poly = boto3.client('polly')

file = open('text.txt')
data = file.read()


def play_sound(text):
    response = poly.synthesize_speech(Text=text, VoiceId='Joanna', OutputFormat='mp3')

    body = response['AudioStream'].read()

    file_name = 'voice.mp3'

    with open(file_name, 'wb') as file:
        file.write(body)
        file.close()

if __name__ == '__main__':
    play_sound(data)
