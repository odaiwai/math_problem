#!/usr/bin/perl
use strict;
use warnings;

# Script to solve a math problem
# dave o'brien 2016/03/24
# problem:
#   A B
# - C D
# -----
#   E F
# + G H
# -----
# P P P
# 
# Where ABCDEFGH, P are all [0-9], and unique
# e.g. AB = 21, if A=2, B=1
#
# Approach: find all values of Where B - D + H = P mod 10, and F is not B, D, or H
