#!/usr/bin/env python3

# Written by Farzeen
# farseenabdulsalam (at) gmail (dot) com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# TLDR;
#   1) I'm not responsible for what you do with this software
#   2) You are allowed to modify and/or use this software as long as you
#      attribute the original work to me

import sys
import random
import pathlib
import configparser
import requests
import argparse

import AppExceptions

VERSION = '1.2 beta'

# Should split to messages of 140 chars each
CHAR_LIMIT = 140
ELLIPSIS = " .. "

DEBUG = True

AUTH_URL = 'http://site21.way2sms.com/Login1.action'
SMS_URL = 'http://site21.way2sms.com/smstoss.action'

##### Read configuration files
# Should be called once before send_sms()
def init_config():
    CONFIG_NAME='way2sms.cfg'
    if not pathlib.Path(CONFIG_NAME).exists():
        raise AppExceptions.ConfigFileNotFoundError(CONFIG_NAME,
                                                 pathlib.Path(CONFIG_NAME).parent)
    try:
        config = configparser.ConfigParser()
        config.read('way2sms.cfg')
        username = config['DEFAULT']['USERNAME']
        password = config['DEFAULT']['PASSWORD']
        return username,password
    except KeyError as e:
        raise AppExceptions.ConfigFileInvalidError(CONFIG_NAME) from e

##### Send SMS
def send_sms(number, message, username, password):
    """
    :type message: str
    :type number : str
    """

    response = requests.post(AUTH_URL,
                data={'username': username, 'password': password},
                allow_redirects=False)

    # If login was successful, cookie JSESSIONID will be set
    if not response.ok or 'JSESSIONID' not in response.cookies:
        raise AppExceptions.Way2SmsAuthError(username)

    # Token is an extract of JSESSIONID
    # It needs to be posted to SMS_URL while sending SMS
    token = response.cookies['JSESSIONID']
    token = token[token.index('~')+1:]

    body = {'Token': token,
           'mobile': number,
           'message': message}

    response = requests.post(SMS_URL,data=body,cookies=response.cookies)

    if response.text.find('successfully') == -1:
        raise AppExceptions.MessageSendingFailedError(
            "Number:{} Message:'{}'".format(number,message))

##### Split message into array of strings of length CHAR_LIMIT
def split_message(message, char_limit, ellipsis):

    message_list = [message]
    if len(message) > char_limit:
        # For first part of message, we do not prepend ellipsis only append.
        char_limit_first = char_limit - len(ellipsis)
        # For subsequent parts message, we prepend and append ellipsis
        char_limit_rest = char_limit - 2*len(ellipsis)

        message_list = [ message[0:char_limit_first] + ellipsis ]
        last_index = char_limit_first
        # // --> floor division
        for i in range( 1, len(message)//char_limit_rest ):
            message_list += [ ellipsis +\
                              message[last_index:last_index+char_limit_rest] +\
                              ellipsis
                            ]
            last_index += char_limit_rest
        else:
            message_list += [ ellipsis +\
                              message[last_index:]
                            ]
    return message_list




def main():
    parser = argparse.ArgumentParser(description="Send SMS using Way2SMS")
    parser.add_argument('-q','--quiet',help='Print nothing to stdout',
                       action='store_true')
    parser.add_argument('numbers',nargs='+',help='Numbers to send sms to')
    parser.add_argument('message',help='Message to send')
    args = parser.parse_args()

    def info(s, **kwargs):
        if not args.quiet:
            print(s,**kwargs)
            sys.stdout.flush()

    try:
        username,password = init_config()
        info("Configuration Read")
        for number in args.numbers:
            info("Sending to '{}' .. ".format(number),end='')
            message_split = split_message(args.message, CHAR_LIMIT, ELLIPSIS)
            total_parts = len(message_split)
            part_index = 1
            for message in message_split:
                info("Sending part {} of {}".format(part_index,total_parts))
                info(message)
                part_index += 1
                send_sms(number,message, username, password)
                info("Success.")

    except AppExceptions.PyWay2SmsError as ex:
        info("Failed")
        print("Error: ",end='',file=sys.stderr)
        print(ex,file=sys.stderr)


if __name__ == '__main__':
    main()
