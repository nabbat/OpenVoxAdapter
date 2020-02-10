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

Import templates from zbx_export_templates.xml and create host like this:
![](https://habrastorage.org/webt/9h/3j/24/9h3j24grdyzjqdhkk2gicho9p1y.png)

![](https://habrastorage.org/webt/2h/pr/-k/2hpr-k6fvrwzrtblyvceu5thgdo.png)
Now you can create graph like this: 

![](https://habrastorage.org/webt/i1/vi/b1/i1vib1uvm3pogak82ufte4myunc.png)

![](https://habrastorage.org/webt/nf/wu/_v/nfwu_v9ep_diohf25-wdlu17mmi.png)

![](https://habrastorage.org/webt/ry/pb/yp/rypbyplx0tjhp9_um4a56x845ma.png)

![](https://habrastorage.org/webt/nz/v6/gs/nzv6gskx6c4tmr1bgiwc9u5ha94.png)

![](https://habrastorage.org/webt/7t/pj/ga/7tpjga93fr6gfmjtkz-6891viiw.png)
