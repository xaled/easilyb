from easilyb.config import get_config_path
print(get_config_path())
print(get_config_path(appname='testapp'))
print(get_config_path(appname='testapp', appauthor='xaled'))

print(get_config_path(appname='testapp', dirpath='/etc/'))
print(get_config_path(appname='testapp', dirpath='/etc/xaled'))
print(get_config_path(appname='testapp', dirpath='/etc/xaled', user_config=True))
print(get_config_path(appname='testapp', dirpath='/etc/xaled', app_root_config=True))
print(get_config_path(appname='testapp', user_config=True, app_root_config=True))
print(get_config_path(appname='testapp', user_config=True, system_config=True))
print(get_config_path(appname='testapp', system_config=True))
