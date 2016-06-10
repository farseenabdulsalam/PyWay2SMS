# PyWay2SMS

Unofficial API that can be used to send SMS using way2sms.com (India Only)

# Configuration

`way2sms.cfg` should contain the following:

    [DEFAULT]
    USERNAME='Your username here'
    PASSWORD='Your password here'
    

# Usage

## Standalone

    usage: PyWay2SMS.py [-h] [-q] numbers [numbers ...] message

    Send SMS using Way2SMS
    
    positional arguments:
      numbers      Numbers to send sms to
      message      Message to send
    
    optional arguments:
      -h, --help   show this help message and exit
      -q, --quiet  Print nothing to stdout

## As a library

* `import PyWay2SMS`
* Do `PyWay2SMS.init_config()
* Send SMS using `PyWay2SMS.send_sms(number, message)`

# LICENSE

## TLDR;
  1) I'm not responsible for what you do with this software.  
  2) You are allowed to modify and/or use this software as long as you attribute
  the original work to me and keep it open source.  
  3) This is an unofficial API. I'm not in anyway affiliated with way2sms.
  I do not intend to violate their trademark or copyright.  
  4) The script may break at any time from now, when there is a change in URL or website structure.
  

## Full Version

Written by Farzeen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
