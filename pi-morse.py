#! /usr/bin/python
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)

def beep (len):
	GPIO.output(22,GPIO.HIGH)
	time.sleep(len)
	GPIO.output(22,GPIO.LOW)
	time.sleep(len)


def a() :
	beep(0.1)
	beep(0.2)

def b() :
	beep(0.2)
	beep(0.1)
	beep(0.1)
	beep(0.1)

def c() :
	beep(0.2)
	beep(0.1)
	beep(0.2)
	beep(0.1)

def d() :
	beep(0.2)
	beep(0.1)
	beep(0.1)

def e() :
	beep(0.1)

def f() :
	beep(0.1)
	beep(0.1)
	beep(0.2)
	beep(0.1)

def g() :
	beep(0.2)
	beep(0.2)
	beep(0.1)

def h() :

	beep(0.1)
	beep(0.1)
	beep(0.1)
	beep(0.1)

def i() :
	beep(0.1)
	beep(0.1)

def j() :
	beep(0.1)
	beep(0.2)
	beep(0.2)
	beep(0.2)

def k() :
	beep(0.2)
	beep(0.1)
	beep(0.2)

def l() :
	beep(0.1)
	beep(0.2)
	beep(0.1)
	beep(0.1)

def m() :
	beep(0.2)
	beep(0.2)

def n() :
	beep(0.2)
	beep(0.1)

def o() :
	beep(0.2)
	beep(0.2)
	beep(0.2)

def p() :
	beep(0.1)
	beep(0.2)
	beep(0.2)
	beep(0.1)

def q() :
	beep(0.2)
	beep(0.2)
	beep(0.1)
	beep(0.2)

def r() :
	beep(0.1)
	beep(0.2)
	beep(0.1)

def s() :
	beep(0.1)
	beep(0.1)
	beep(0.1)

def t() :
	beep(0.2)

def u() :
	beep(0.1)
	beep(0.1)
	beep(0.2)

def v() :
	beep(0.1)
	beep(0.1)
	beep(0.1)
	beep(0.2)
	
def w() :
	beep(0.1)
	beep(0.2)
	beep(0.2)

def x() :
	beep(0.2)
	beep(0.1)
	beep(0.1)
	beep(0.2)

def y() :
	beep(0.2)
	beep(0.1)
	beep(0.2)
	beep(0.2)
	
def z() :
	beep(0.2)
	beep(0.2)
	beep(0.1)
	beep(0.1)

def doNothing() :
	time.sleep(0.2)

morse = {'a' : a,
	'b' : b,
	'c' : c,
	'd' : d,
	'e' : e,
	'f' : f,
	'g' : g,
	'h' : h,
	'i' : i,
	'j' : j,
	'k' : k,
	'l' : l,
	'm' : m,
	'n' : n,
	'o' : o,
	'p' : p,
	'q' : q,
	'r' : r,
	's' : s,
	't' : t,
	'u' : u,
	'v' : v,
	'w' : w,
	'x' : x,
	'y' : y,
	'z' : z,
	' ' : doNothing,
}
message = raw_input("What should I beep out in morse? ").lower()
for c in message:
	morse[c]()
	time.sleep(0.1)
