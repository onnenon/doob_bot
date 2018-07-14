install_python_36:
  pkg.installed:
    - sources:
      pkg.installed:
    - sources:
      {% set os = 'centos' if grains['os'] == 'CentOS' else 'rhel' -%}
      - ius-release: https://{{ os }}{{ grains['osmajorrelease'] }}.iuscommunity.org/ius-release.rpm

install_python_package:
  pkg.installed:
    - pkgs:
      - python36u
      - python36u-pip

get_repo:
  git.latest:
    - name: https://github.com/onnenon/doob_bot.git
    - user: sonnen
    - target: /home/sonnen/projects/doob
    - force_reset: True

set_bot_token_env_variable:
  file.append:
    - name: /etc/systemd/system.conf
    - text: DefaultEnvironment="BOT_TOKEN={{ pillar['bot_token'] }}"

install_requirements:
  cmd.run:
    - name: pip3.6 install -r /home/sonnen/projects/doob/requirements.txt

upstart_conf:
  file.managed:
    - name: /etc/systemd/system/doob_bot.service
    - source: salt://bot/doob_bot.service

enable_bot_service:
  service.running:
    - name: doob_bot.service
    - enable: True
    - reoload: True
