# 'sqlite+pysqlite:///:memory:'
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "vk1.a.Yhjyr9d_fPpPtRJBPoZ2_qYbjtK8EWnmdOye1E8oZ_-oQXEq-jIBoiVPaM-CI_YoHO1Z4LiIRI0yP3XaIiKHFX10vxKwoSsBqSPRlwDYAsKIC26y7_nMLkvMk0C9QNTA7_dI9GAXBe8USD_1thp4CDm7uyY0Hsm04TnGLuypaiBMygEdAPkK8pHw4xd4FTqTGQ_-4KIE7UE6lrVh8HEHwg"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

keyboard_ = VkKeyboard(one_time=True)
keyboard_.add_button('Привет', color=VkKeyboardColor.SECONDARY)


def send_message(text, keyboard=None):
    message = text
    user_id = event.user_id
    if keyboard is None:
        vk.messages.send(
            message=message,
            user_id=user_id,
            random_id=random.randint(-10 ** 7, 10 ** 7),
            # keyboard=keyboard.get_keyboard()
        )
    else:
        vk.messages.send(
            message=message,
            user_id=user_id,
            random_id=random.randint(-10 ** 7, 10 ** 7),
            keyboard=keyboard.get_keyboard()
        )


for event in longpoll.listen():
    # print(event)
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_mes = event.text.lower()
        if user_mes == 'клава':
            send_message('Ну привет)', keyboard_)
        elif user_mes == 'пока':
            send_message('Ну пока)')
            exit()
        else:
            send_message('I do not no)')
