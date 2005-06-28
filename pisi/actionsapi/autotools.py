#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pisi.context import const

def configure(parameters = ''):
    ''' FIXME: Düzgün hale getirilecek '''
    ''' parameters = '--with-nls --with-libusb --with-something-usefull '''

    configure_string = './configure --prefix=/usr \
                --host=i686-pc-linux-gnu \
                --mandir=/usr/share/man \
                --infodir=/usr/share/info \
                --datadir=/usr/share \
                --sysconfdir=/etc \
                --localstatedir=/var/lib \
                %s' % parameters

    os.system(configure_string)

def make():
    ''' FIXME: Düzgün hale getirilecek '''
    os.system('make')

def install():
    ''' FIXME: Düzgün hale getirilecek '''
    ''' dir_suffix = /var/tmp/pisi/ _paket_adı_ /image/ '''
    global const

    dir_suffix = os.path.dirname(os.path.dirname(os.getcwd())) + \
        const.install_dir_suffix

    install_string = 'make prefix=%(prefix)s/usr \
                datadir=%(prefix)s/usr/share \
                infodir=%(prefix)s/usr/share/info \
                localstatedir=%(prefix)s/var/lib \
                mandir=%(prefix)s/usr/share/man \
                sysconfdir=%(prefix)s/etc \
                install' % {'prefix': dir_suffix}

    os.system(install_string)
