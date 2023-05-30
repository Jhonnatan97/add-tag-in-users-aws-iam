import boto3


def adicionar_tag_usuarios_iam():
    boto3.setup_default_session (profile_name='<your-profile>')
    users = []

    # Crie uma instância do cliente IAM
    iam = boto3.client ('iam')

    # Lista todos os usuários do IAM
    response = iam.list_users ()
    users.extend (response['Users'])
    while 'Marker' in response.keys ():
        response = iam.list_users (Marker=response['Marker'])
        users.extend (response['Users'])
    print (f'Total usuários: {len (users)}')

    # Adicione a tag aos usuários
    for user in users:
        username = user.get('UserName')

        # Verifique se o usuário já possui a tag
        tags_response = iam.list_user_tags (UserName=username)
        tags = tags_response['Tags']
        tag_status_exists = any (tag['Key'] == 'tag_status' for tag in tags)

        # Se o usuário já tiver a tag, pule para o próximo usuário
        if tag_status_exists:
            print (f"O usuário {username} já possui a tag 'tag_status'.")
            continue

        # Adicione a tag ao usuário
        response = iam.tag_user (
            UserName=username,
            Tags=[
                {
                    'Key': 'tag_status',
                    'Value': 'TRUE'
                },
            ]
        )

        # Verifique se a tag foi adicionada com sucesso
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print (f"A tag 'tag_status' foi adicionada ao usuário {username}.")
        else:
            print (f"A tag 'tag_status' não pôde ser adicionada ao usuário {username}.")


# Chame a função para adicionar a tag aos usuários
adicionar_tag_usuarios_iam ()
