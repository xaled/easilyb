import re
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits, \
    printable, punctuation, whitespace
safe0 = ascii_letters + digits + '_'
safe1 = safe0 + '.-'


def validate_charset(line, charset):
    for c in line:
        if c not in charset:
            return False
    return True


# -----------------------------------------------------------------------------------
# Credit: Konsta Vesterinen (github.com/kvesteri) LICENSE: MIT
DOMAIN_PATTERN = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)
# The MIT License (MIT)
#
# Copyright (c) 2013-2014 Konsta Vesterinen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# -----------------------------------------------------------------------------------


def validate_domain(domain):
    if DOMAIN_PATTERN.match(domain) is not None:
       return True
    return False

from easilyb.validators.ip import validate_ip, validate_ipv4, validate_ipv6

