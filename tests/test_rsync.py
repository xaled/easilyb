from easilyb.commands.rsync import Rsync
rsync = Rsync('/home/xaled/Desktop/easilyb', 'user@host', '/apps/easilyb')
rsync.profiles_options['direct']['remote_commands'] = ['ls -alh /apps']
rsync.main()