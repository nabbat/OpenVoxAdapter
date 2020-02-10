# OpenVoxAdapter
![OpenVox](https://hsto.org/getpro/habr/post_images/d70/867/071/d708670711697112973c26527f0cd0c0.jpg)
You can receive data from the gateway OpenVox without using HTTP Digest Auth
<http://ip_adapter:9090/?ip=ip_OpenVox&board=1&port=3&obj=signal>
for example, to monitor SIM settings in Zabbix.
On the gateway must be installed login and password 'admin' 'admin' or you can edit code.

//TODO login and password to settings.

# Parameters:

- 6 < board = 1
- port > 0
- obj =
    - port,
    - d-channel
    - status
    - type
    - manufacturer
    - model_name
    - model_imei
    - revision
    - operator
    - register
    - signal
    - ber
    - sim_imsi
    - sim_sms_center_number
    - own_number
    - remain_time
    - pdd
    - asr
    - acd
    - last_event
    - state
    - last_send_at
    - show_status
