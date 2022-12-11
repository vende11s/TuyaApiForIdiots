# what is TuyaApiForIdiots?
* python code for steering tuya light bulbs
* it's wrapper of wrapper of wrapper
* every idiot can use it, it couldn't be more simple

# usage
* connect your bulb to Tuya app
* go to Tuya iot, create project, add device, you'll find at the internet how to do it
* find ip of your bulb, you can use nmap: `sudo nmap -sn 192.168.<>.<>/24` or some android app
* (optional but recommended) go to your router->dhcp settings and set constant ip for your bulb
* install [tuya cli](https://github.com/TuyaAPI/cli) `npm i @tuyapi/cli -g`
* run `tuya-cli wizard`, use keys from Tuya iot, grab device key
* put id, key and ip to `tuya.py` (and maybe protocol version, when i'm writing it the actual version is 3.3)
* run `tuya.py -h` to learn possible options
* And that's it! You can steer tuya light bulb from pc in the easiest way possible!
