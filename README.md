# cbpi-Wii
This plugin extends the [CraftBeerPi](https://github.com/Manuel83/craftbeerpi3) software by a [sensor](https://github.com/Manuel83/craftbeerpi3/wiki/Custom-Sensor) in order to monitor weight changes _(KG/LBS)_ using a [Nintento Wii Balance Board](https://en.wikipedia.org/wiki/Wii_Balance_Board). The plugin heavily uses an [extended version](https://github.com/peakMeissner/gr8w8upd8m8) of the [Gr8W8Upd8M8](https://github.com/skorokithakis/gr8w8upd8m8) script created by [skorokithakis](https://github.com/skorokithakis) and is therefore licenced under [LGPL 3.0](https://www.gnu.org/licenses/lgpl.html).

## Requirements
- Linux _(i.e. [Raspbian](https://en.wikipedia.org/wiki/Raspbian))_
- The [bluez-utils](https://packages.debian.org/de/wheezy/bluez-utils) package
- [CraftBeerPi V3](https://github.com/Manuel83/craftbeerpi3/tree/master/modules)
- Bluetooth enabled hardwear _(i.e. [Raspberry Pi 3 model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/))_

## Installation
    cd craftbeerpi3/modules/plugins/
    git clone https://github.com/peakMeissner/cbpi-MQTTClient
    cd cbpi-MQTTClient

## Sample Implementation
![](https://raw.githubusercontent.com/peakMeissner/cbpi-Wii/master/docs/img/sample.jpg)
