from config import MODERATOR_LOGIN, MODERATOR_PASSWORD
from framework.client import Client

client = Client()


def delete_posts_by_moder():
    all_feed = client.get_feed(0, 300).json()['Result']
    list_to_delete = []
    for i in range(len(all_feed)):
        try:
            if 'Auto-title' in all_feed[i]['Article']['Article']['Title']:
                list_to_delete.append(all_feed[i]['Article']['Article']['ID'])
        except:
            pass
        try:
            if 'Auto-title' in all_feed[i]['Question']['Question']['Title']:
                list_to_delete.append(all_feed[i]['Question']['Question']['ID'])
        except:
            pass
    body = {
        "Login": MODERATOR_LOGIN,
        "Password": MODERATOR_PASSWORD
    }
    response = client.post_login(body)
    resp_2 = response.json()['Credentials']['Token']
    collect = 0
    reg = {
        'Authorization': f'{resp_2}'
    }
    for i in range(len(list_to_delete)):
        try:
            client.delete_question(list_to_delete[i], reg)
            if client.get_questions(list_to_delete[i]).json()['Result']['Question']['Status'] == 'REMOVED_BY_MODERATOR':
                collect += 1
                print(f'- Question пост. {collect}')
        except:
            pass
        try:
            client.delete_article(list_to_delete[i], reg)
            if client.get_article(list_to_delete[i]).json()['Result']['Article']['Status'] == 'REMOVED_BY_MODERATOR':
                collect += 1
                print(f'- Article пост {collect}')
        except:
            pass
    return print('Ну как, вышло?')


delete_posts_by_moder()


''' + Переменные окружения

    test-01:
        APP_DIR=D:\for_py_test
        URL=http://toci-test-01.aurora
        API_URL=http://toci-test-01.aurora:8080
        MODER_LOGIN=moder_moder
        MODER_PASSWORD=Lubamovi4

    test-02:
        APP_DIR=D:\for_py_test
        URL=http://toci-test-02.aurora
        API_URL=http://toci-test-02.aurora:8080
        MODER_LOGIN=Test@testingCool.omg
        MODER_PASSWORD=Llkjdhdffasfas
    
    preprod:
        APP_DIR=D:\for_py_test
        URL=https://toci-preprod-01.aurora
        API_URL=http://toci-backend-preprod-01.aurora:8080
        MODER_LOGIN=Test@testingCool.omg
        MODER_PASSWORD=Lubamovi4
    
'''



