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
# Where ABCDEFGH, P are all [1-9], and unique
# e.g. AB = 21, if A=2, B=1
#
# Approach: find all values of Where B - D + H = P mod 10, and F is not B, D, or H

#my @numbers; # array to hold the numbers
#my @stack; # array holding a partial stack, i.e. B, D, F, H, P

# Try a brute force solution:
# iterate over every possible value of a, b, c, d, g, h (e, f are calculated), 
foreach my $a (1..9) {
	foreach my $b (1..9) {
		foreach my $c (1..9) {
			foreach my $d (1..9) {
				my $ab = (10 * $a + $b);
				my $cd = (10 * $c + $d);
				# Calculate E, F
				my $ef = ( $ab - $cd);
				my $e = int($ef/10);
				my $f = substr(sprintf("%00d", $ef),-1,1);
				foreach my $g (1..9) {
					foreach my $h (1..9) {
						# Check if all 8 numbers are unique before proceeding
						if (numbers_ok($a, $b, $c, $d, $e, $f, $g, $h)) {
							my $gh = (10 * $g + $h);
							my $ppp = $ef + $gh;
							# Get each value of P by making a string of PPP: 000
							my $ppp_char = sprintf("%03d", $ppp);
							my $p1 = substr($ppp_char, 0, 1);
							my $p2 = substr($ppp_char, 1, 1);
							my $p3 = substr($ppp_char, 2, 1);
							if ( ($p1 eq $p2) and ($p2 eq $p3)) {
								print "($a, $b), ($c, $d): $ab - $cd = $ef ($e, $f), ($g, $h), $gh = $ppp ($ppp_char: $p1, $p2, $p3)\n";
							}
						}
					}
				}
			}
		}
	}
}

## Subroutines:
sub max {
	# sub to return the maximum value from a list
	my $max = shift; # maximum is initially the first number
	# Iterate through the list of numbers given, finding the maximum one.
	while (my $num = shift) {
		if ($num>$max) { $max = $num;}
	}
	return $max;
}

sub numbers_ok {
	#receives a list of numbers and returns 1 if no duplicates, 0 otherwise
	my $result = 1; # default result
	my %count; # Hash (Associative Array) of numbers
	my $debug = 0;
	# Iterate through the array of numbers given (special array @_, 
	# shift removes an element from the array, and passes it to a variable):
	while (my $number = shift) {
		$count{$number}++; # 
		print "$number ($count{$number}) " if $debug;
		if ($count{$number}>1) {
			$result = 0;
		}
	}
	print "\n" if $debug;
	return $result;
}
