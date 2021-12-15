M, N, K = map(int, input().split())

secret_menu = ''.join(input().split(' '))
user_button = ''.join(input().split(' '))
if len(secret_menu) <= len(user_button) and secret_menu in user_button:
    print('secret')
else:
    print('normal')