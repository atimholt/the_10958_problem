#! /usr/bin/env python

from shutil import copyfile
from subprocess import call
import os
import platform

VERSION='0.0.0'
APPNAME='the_10958_problem'

top = '.'
out = 'bin'

def options(opt):
    opt.load('compiler_cxx')

def configure(conf):
    conf.env.MSVC_TARGETS = ['x64']
    conf.env.CXXFLAGS = ['/nologo', '/EHsc', '/MD']
    conf.load('compiler_cxx msvc')

def post(ctx):
    print("\n -- Running Unit tests: --\n")
    call(['./bin/rational_geometry_test.exe'])
    print("\n -- End Unit tests --\n")

def build(bld):
    my_source = ['main.cpp']

    bld.program(
            source   = my_source,
            features = 'cxx cxxprogram',
            target   = 'the_10958_problem')

    # bld.add_post_fun(post)

# vim:set et ts=4 sts=4 sw=4 ft=python:

