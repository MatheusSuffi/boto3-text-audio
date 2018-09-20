import boto3

#a variavel region representa o pt-BR ou en-US (verifique no site da aws para ter todas as regioes)
region = 'sa-east-1'

#a variavel voiceid serve para escolher a voz que ira falar o texto. Lembrando que cada voz fala em uma lingua diferente (verifique o site da aws para ter todas as vozes)
voice = 'Ricardo'

texto = 'INSIRA SEU TEXTO AQUI'

polly_client = boto3.Session(
    aws_secret_access_key='CHAVE_AMAZON'
    aws_access_key_id='SENHA_CHAVE_AMAZON',
    region_name=region).client('polly')

response = polly_client.synthesize_speech(VoiceId=voice,
                OutputFormat='mp3', 
                Text = texto)

#Aqui ele le o audio e salve ele no caminho e com o nome de sua escolha
file = open('CAMINHO/NOME_AUDIO.mp3', 'w')
file.write(response['AudioStream'].read())
file.close()
