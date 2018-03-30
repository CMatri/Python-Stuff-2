# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
#   
#   MAC:
#   python3 <thisfile.py> <your_one_file.py>
# 
#   PC:
#   python <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2
# 
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
# 
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.


import unittest
import shutil
import sys
import os
import time

#import subprocess

import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = ["Invitation",
				  "Response",
				  "InviteNotFoundError",
				  "TooManyError",
				  "Event",
				 ]

# for method names in classes that will be tested. They have to be here
# so that we don't complain about missing global function definitions.
# Really, any chosen name for test batches can go here regardless of actual
# method names in the code.
SUB_DEFNS = [
				"find_invite",
				"pop_invite",
				"add_invite",
				"find_response",
				"pop_response",
				"read_response",
				"count_attendees",
				"count_rejections",
				"max_attendance",
				"count_pending",
				"rescind_invitation",
			]

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = [ ]

# how many points are test cases worth?
weight_required     = 1
weight_extra_credit = 1

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 100

# how many seconds to wait between batch-mode gradings? 
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode... 
CURRENTLY_GRADING = False


# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"


# END SPECIALIZATION SECTION

################################################################################
################################################################################
################################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
		
    ############################################################################
	
	def test_Invitation_1(self):
		"""Invitation init"""
		i = Invitation("Alice",3)
		self.assertEqual(i.name, "Alice")
		self.assertEqual(i.num_invited, 3)
	
	def test_Invitation_2(self):
		"""Invitation str"""
		i = Invitation("Alice",3)
	
	def test_Invitation_3(self):
		"""Invitation repr"""
		i = Invitation("Bob",7)
		self.assertEqual(str(i),"Invitation('Bob', 7)")
	
	def test_Invitation_4(self):
		"""Invitation eq"""
		i = Invitation("Carol",4)
		self.assertEqual(repr(i),"Invitation('Carol', 4)")
	
	def test_Invitation_5(self):
		"""Invitation eq"""
		i1 = Invitation("Degas",1)
		i2 = Invitation("Enid",8)
		i3 = Invitation("Enid",8)
		self.assertNotEqual(i1, i2)
		self.assertEqual(i2,i3)
		self.assertEqual(i1,i1)
	
	def test_Invitation_6(self):
		"""Invitation lt"""
		i1 = Invitation("Farooq",1)
		i2 = Invitation("Giert",8)
		self.assertTrue(i1<i2)
		self.assertFalse(i2<i1)
	
	def test_Invitation_7(self):
		"""Invitation lt"""
		i1 = Invitation("Harriet",9)
		i2 = Invitation("Harriet",12)
		self.assertTrue(i1<i2)
		self.assertFalse(i2<i1)
	
	def test_Invitation_8(self):
		"""Invitation lt"""
		i1 = Invitation("Inigo",15)
		i2 = Invitation("Inigo",15)
		self.assertFalse(i1<i2)
		self.assertFalse(i2<i2)
		
    ########################################################################### 
	
	def test_Response_1 (self):
		"""Response init"""
		r = Response("Jackie", True, 2)
		self.assertEqual(r.name, "Jackie")
		self.assertEqual(r.ans, True)
		self.assertEqual(r.num_attending,2)
		r2 = Response("Amy",False,0)
		self.assertEqual(r2.name,"Amy")
		self.assertEqual(r2.ans,False)
		self.assertEqual(r2.num_attending,0)
	
	def test_Response_2 (self):
		"""Response str"""
		r = Response("Khalid",True, 5)
		self.assertEqual(str(r), "Response('Khalid', True, 5)")
		r2 = Response("Layla",False, 0)
		self.assertEqual(str(r2), "Response('Layla', False, 0)")
	
	def test_Response_3 (self):
		"""Response repr"""
		r = Response("Khalid",True, 5)
		self.assertEqual(repr(r), "Response('Khalid', True, 5)")
		r2 = Response("Layla",False, 0)
		self.assertEqual(repr(r2), "Response('Layla', False, 0)")
	def test_Response_4 (self):
		"""Response eq"""
		r1 = Response("Khalid",True, 5)
		r2 = Response("Layla",False, 0)
		r3 = Response("Layla",False, 0)
		self.assertTrue(r1==r1)	
		self.assertTrue(r2==r3)
		self.assertFalse(r1==r2)
	def test_Response_5 (self):
		"""Response lt"""
		r0 = Response("Mark",True,3)
		r1 = Response("Nessie",False,2)
		self.assertTrue(r0 < r1)
	def test_Response_6 (self):
		"""Response lt"""
		r1 = Response("Nessie",False,0)
		r2 = Response("Nessie",True,2)
		r3 = Response("Nessie",True,3)
		self.assertTrue (r1 < r2)
		self.assertTrue (r2 < r3)
		self.assertFalse(r2 < r1)
		self.assertFalse(r3 < r2)
	
	def test_Response_7 (self):
		"""Response lt"""
		rA = Response("A",True,2)
		rB = Response("A",True,2)
		self.assertFalse(rA<rB)
	
    ########################################################################### 

	def test_InviteNotFoundError_1 (self):
		"""InviteNotFoundError init"""
		inf1 = InviteNotFoundError('test')
		self.assertEqual(inf1.name, 'test')
		inf2 = InviteNotFoundError('asdfasdfasdf')
		self.assertEqual(inf2.name, 'asdfasdfasdf')
	
	def test_InviteNotFoundError_2 (self):
		"""InviteNotFoundError str"""
		inf1 = InviteNotFoundError('test')
		inf2 = InviteNotFoundError('asdfasdfasdf')
		self.assertEqual(str(inf1),"no invite for 'test' found.")
		self.assertEqual(str(inf2),"no invite for 'asdfasdfasdf' found.")
	
	def test_InviteNotFoundError_3 (self):
		"""InviteNotFoundError repr"""
		inf1 = InviteNotFoundError('test')
		inf2 = InviteNotFoundError('asdfasdfasdf')
		self.assertEqual(repr(inf1),"InviteNotFoundError('test')")
		self.assertEqual(repr(inf2),"InviteNotFoundError('asdfasdfasdf')")
	
	def test_InviteNotFoundError_4 (self):
		"""InviteNotFoundError eq"""
		inf1 = InviteNotFoundError('test')
		inf2 = InviteNotFoundError('test')
		self.assertTrue(inf1==inf2)
	
	def test_InviteNotFoundError_5 (self):
		"""InviteNotFoundError eq"""
		inf1 = InviteNotFoundError('test')
		inf2 = InviteNotFoundError('asdfasdfasdf')
		self.assertFalse(inf1==inf2)	
	
    ########################################################################### 
	
	def test_TooManyError_1 (self):
		"""TooManyError init"""
		e1 = TooManyError(5,3)
		e2 = TooManyError(2,1)
		self.assertEqual(e1.num_requested,5)
		self.assertEqual(e1.num_allowed, 3)
		self.assertEqual(e2.num_requested,2)
		self.assertEqual(e2.num_allowed, 1)
		
	def test_TooManyError_2 (self):
		"""TooManyError str"""
		e1 = TooManyError(5,3)
		e2 = TooManyError(2,1)
		self.assertEqual(str(e1),"too many: 5 requested, 3 allowed.")
		self.assertEqual(str(e2),"too many: 2 requested, 1 allowed.")
	
	def test_TooManyError_3 (self):
		"""TooManyError repr"""
		e1 = TooManyError(5,3)
		e2 = TooManyError(2,1)
		self.assertEqual(repr(e1),"TooManyError(5, 3)")
		self.assertEqual(repr(e2),"TooManyError(2, 1)")
	
	def test_TooManyError_4 (self):
		"""TooManyError eq"""
		e1 = TooManyError(10,9)
		e2 = TooManyError(8,5)
		e3 = TooManyError(10,9)
		self.assertTrue(e1==e3)
		self.assertFalse(e1==e2)
		self.assertFalse(e2==e3)
		
	def test_TooManyError_5 (self):
		"""TooManyError eq"""
		e1 = TooManyError(7,5)
		e2 = TooManyError(7,5)
		e3 = e1
		e4 = TooManyError(100,6)
		self.assertTrue(e1==e2)
		self.assertTrue(e1==e3)
		self.assertTrue(e2==e3)
		self.assertFalse(e1==e4)
		self.assertFalse(e2==e4)
		self.assertFalse(e3==e4)
	
    ########################################################################### 
    
	def test_Event_1 (self):
		"""Event init"""
		e = Event('gig', [Invitation('a',1),Invitation('b',2)], [Response('b',True,1)])
		self.assertEqual(e.title, "gig")
		self.assertEqual(e.invites,   [Invitation('a',1),Invitation('b',2)])
		self.assertEqual(e.responses, [Response('b',True,1)])
		
		e2 = Event('birthday', [Invitation('A',3),Invitation('B',4)], [Response('A',False,0)])
		self.assertEqual(e2.title, "birthday")
		self.assertEqual(e2.invites,   [Invitation('A',3),Invitation('B',4)])
		self.assertEqual(e2.responses, [Response('A',False,0)])
		
	def test_Event_2 (self):
		"""Event init"""
		e = Event('halloween party', [], [])
		self.assertEqual(e.title, "halloween party")
		self.assertEqual(e.invites,   [])
		self.assertEqual(e.responses, [])
	
	def test_Event_3 (self):
		"""Event init"""
		e = Event("Indigenous People's Day")
		self.assertEqual(e.title, "Indigenous People's Day")
		self.assertEqual(e.invites,   [])
		self.assertEqual(e.responses, [])
		
	def test_Event_4 (self):
		"""Event str"""
		e1 = Event('gig', [Invitation('a',1),Invitation('b',2)], [Response('b',True,1)])
		e2 = Event('birthday', [Invitation('A',3),Invitation('B',4)], [Response('A',False,0)])
		self.assertEqual(str(e1),"Event('gig', [Invitation('a', 1), Invitation('b', 2)], [Response('b', True, 1)])")
		self.assertEqual(str(e2),"Event('birthday', [Invitation('A', 3), Invitation('B', 4)], [Response('A', False, 0)])")
	
	def test_Event_5 (self):
		"""Event repr"""
		e0 = Event('boring', [], [])
		e1 = Event('gig', [Invitation('a',1),Invitation('b',2)], [Response('b',True,1)])
		e2 = Event('birthday', [Invitation('A',3),Invitation('B',4)], [Response('A',False,0)])
		self.assertEqual(repr(e0),"Event('boring', [], [])")
		self.assertEqual(repr(e1),"Event('gig', [Invitation('a', 1), Invitation('b', 2)], [Response('b', True, 1)])")
		self.assertEqual(repr(e2),"Event('birthday', [Invitation('A', 3), Invitation('B', 4)], [Response('A', False, 0)])")
	
	def test_Event_6 (self):
		"""Event eq"""
		e0  = Event('boring', [], [])
		e1a = Event('gig', [Invitation('a',1),Invitation('b',2)], [Response('b',True,1)])
		e1b = Event('gig', [Invitation('a',1),Invitation('b',2)], [Response('b',True,1)])
		e2  = Event('birthday', [Invitation('A',3),Invitation('B',4)], [Response('A',False,0)])
		self.assertTrue(e1a==e1b)
		self.assertTrue(e0==e0)
		self.assertFalse(e0==e1a)
		self.assertFalse(e1a==e2)
	
	def test_Event_7 (self):
		"""Event eq"""
		e1 = Event('gig', [Invitation('a',1),Invitation('b',2)], [Response('b',True,1)])
		e2 = Event('birthday', [Invitation('A',3),Invitation('B',4)], [Response('A',False,0)])
		self.assertFalse(e1==e2)
		e1.title = e2.title
		e1.invites = e2.invites
		e1.responses = e2.responses
		self.assertTrue(e1==e2)
	
	def test_Event_8 (self):
		"""sorting incoming lists to Event::__init__"""
		e1 = Event('concert',[Invitation("B",5),Invitation("A",3)], [Response("B",True, 4), Response("A",False,0)])
		invs = [Invitation("A",3),Invitation("B",5)]
		rs   = [Response("A",False,0), Response("B",True, 4)]
		self.assertEqual(e1.invites, invs)
		self.assertEqual(e1.responses, rs)
	
    ########################################################################### 
	
	def test_find_invite_1 (self):
		"""find_invite: present (only one)."""
		inv = Invitation("zed",26)
		e = Event('gig', [inv],[])
		i = e.find_invite('zed')
		self.assertEqual(inv, i)
		self.assertEqual(id(inv), id(i))
			
	def test_find_invite_2 (self):
		"""find_invite: present at beginning."""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		e = Event('gig', invs,[])
		i = e.find_invite('Drew')
		self.assertEqual(invs[0], i)
		self.assertEqual(id(invs[0]), id(i))
	
	def test_find_invite_3 (self):
		"""find_invite: present in middle."""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		e = Event('gig', invs,[])
		i = e.find_invite('Shrek')
		self.assertEqual(invs[2], i)
		self.assertEqual(id(invs[2]), id(i))
	
	def test_find_invite_4 (self):
		"""find_invite: present at end."""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		e = Event('gig', invs,[])
		i = e.find_invite('zed')
		self.assertEqual(invs[3], i)
		self.assertEqual(id(invs[3]), id(i))
	
# 	def test_find_invite_5 (self):
# 		"""find_invite: not present; raises InviteNotFoundError"""
# 		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
# 		e = Event('gig', invs,[])
# 		try:
# 			i = e.find_invite('Godot')
# 			self.fail("should have raised InviteNotFoundError because we will wait forever for Godot.")
# 		except InviteNotFoundError:
# 			pass
		
	def test_find_invite_5 (self):
		"""find_invite: empty list (raises InviteNotFoundError)"""
		invs = []
		e = Event('gig', invs,[])
		try:
			i = e.find_invite('Ever')
			self.fail("should have raised InviteNotFoundError because we will wait forever for Ever.")
		except InviteNotFoundError:
			pass
		
	def test_find_invite_6 (self):
		"""find_invite: check list is unchanged when invite found."""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		invs_copy = invs[:]
		e = Event('gig', invs,[])
		i = e.find_invite('Drew')
		self.assertEqual(invs[0], i)
		self.assertEqual(id(invs[0]), id(i))
		self.assertEqual(invs_copy, e.invites)
	
	def test_find_invite_7 (self):
		"""find_invite: check list is unchanged when invite not found."""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		invs_copy = invs[:]
		e = Event('gig', invs,[])
		try:
			i = e.find_invite('not present')
		except:
			pass
		self.assertEqual(invs_copy, e.invites)
	
    ########################################################################### 
	
	def test_pop_invite_1 (self):
		"""pop_invite: present(first)"""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		e = Event('gig', invs,[])
		i = e.pop_invite('Drew')
		self.assertEqual(Invitation("Drew",1), i)
		self.assertEqual(e.invites, [Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)])
	
	def test_pop_invite_2 (self):
		"""pop_invite: present(middle)"""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		e = Event('gig', invs,[])
		i = e.pop_invite('Pattie')
		self.assertEqual(Invitation("Pattie",21), i)
		self.assertEqual(e.invites, [Invitation("Drew",1),Invitation("Shrek",24),Invitation("zed",26)])
	
	def test_pop_invite_3 (self):
		"""pop_invite: not found (raises InviteNotFoundError)"""
		invs = [Invitation("Drew", 1),Invitation("Pattie",21),Invitation("Shrek",24),Invitation("zed",26)]
		e = Event('gig', invs,[])
		try:
			i = e.pop_invite('Jaime')
			self.fail ("should have raised InviteNotFound, because Jaime isn't there.")
		except InviteNotFoundError:
			pass
	
	def test_pop_invite_4 (self):
		"""pop_invite: empty list (raises InviteNotFoundError)"""
		invs = []
		e = Event('gig', invs,[])
		try:
			i = e.pop_invite('Jaime')
			self.fail ("should have raised InviteNotFound, because Jaime isn't there.")
		except InviteNotFoundError:
			pass
	
	def test_pop_invite_5 (self):
		"""pop_invite: also removes Responses of same name."""
		e = Event("thing", [Invitation("A",1),Invitation("B",2)], [Response("A",True,1),Response("B",True,1)])
		i = e.pop_invite("A")
		self.assertEqual(i,Invitation("A",1))
		self.assertEqual(e.invites,[Invitation("B",2)])
		self.assertEqual(e.responses, [Response("B",True,1)])
	
    ########################################################################### 
	
	def test_add_invite_1 (self):
		"""add_invite: added (only item)"""
		e = Event("wedding",[],[])
		inv = Invitation("Fabio",3)
		e.add_invite(inv)
		self.assertEqual(e.invites, [inv])
		
	def test_add_invite_2 (self):
		"""add_invite: added (to middle of list)"""
		e = Event("wedding",[Invitation("Andrew",2),Invitation("Jerzy",4)],[])
		inv = Invitation("Fabio",3)
		e.add_invite(inv)
		self.assertEqual(e.invites, [Invitation("Andrew",2),Invitation("Fabio",3),Invitation("Jerzy",4)])
	
	def test_add_invite_3 (self):
		"""add_invite: added (to end of list)"""
		e = Event("wedding",[Invitation("Andrew",2),Invitation("Jerzy",4)],[])
		inv = Invitation("Yoders",3)
		e.add_invite(inv)
		self.assertEqual(e.invites, [Invitation("Andrew",2),Invitation("Jerzy",4),Invitation("Yoders",3)])
	
	def test_add_invite_4 (self):
		"""add_invite: replaces old one (at beginning)"""
		e = Event("wedding",[Invitation("Andrew",2),Invitation("Fabio",3), Invitation("Jerzy",4)],[])
		inv = Invitation("Andrew",8)
		e.add_invite(inv)
		self.assertEqual(e.invites, [Invitation("Andrew",8),Invitation("Fabio",3),Invitation("Jerzy",4)])
	
	def test_add_invite_5 (self):
		"""add_invite: replaces old one (in middle)"""
		e = Event("wedding",[Invitation("Andrew",2),Invitation("Fabio",3), Invitation("Jerzy",4)],[])
		inv = Invitation("Fabio",5)
		e.add_invite(inv)
		self.assertEqual(e.invites, [Invitation("Andrew",2),Invitation("Fabio",5),Invitation("Jerzy",4)])
	
	def test_add_invite_6 (self):
		"""add_invite: replaces old one (at end)"""
		e = Event("wedding",[Invitation("Andrew",2),Invitation("Fabio",3), Invitation("Jerzy",4)],[])
		inv = Invitation("Jerzy",8)
		e.add_invite(inv)
		self.assertEqual(e.invites, [Invitation("Andrew",2),Invitation("Fabio",3),Invitation("Jerzy",8)])
	
	def test_add_invite_7 (self):
		"""add_invite: replace only item."""
		e = Event("wedding",[Invitation("Andrew",2)],[])
		inv = Invitation("Andrew",8)
		e.add_invite(inv)
		self.assertEqual(e.invites, [Invitation("Andrew",8)])
	
	########################################################################### 
	
	def test_find_response_1 (self):
		"""find_response: present(only one)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3)]
		e = Event("Snow Ball", invs, resps)
		r = e.find_response("R")
		self.assertEqual(r, Response("R",True,3))
	
	def test_find_response_2 (self):
		"""find_response: present(first)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		r = e.find_response("R")
		self.assertEqual(r, Response("R",True,3))
	
	def test_find_response_3 (self):
		"""find_response: present(middle)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		r = e.find_response("S")
		self.assertEqual(r, Response("S",True,2))
	
	def test_find_response_4 (self):
		"""find_response: present(end)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		r = e.find_response("T")
		self.assertEqual(r, Response("T",False,0))
	
	def test_find_response_5 (self):
		"""find_response: not found (raises LookupError)"""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		try:
			r = e.find_response("ghost")
			self.fail("should have raised a LookupError, no ghost here!")
		except LookupError:
			pass
	
	def test_find_response_6 (self):
		"""find_response: empty list (raises LookupError)"""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = []
		e = Event("Snow Ball", invs, resps)
		try:
			r = e.find_response("ghost")
			self.fail("should have raised a LookupError, no ghost here! (empty list of responses)")
		except LookupError:
			pass
	
	########################################################################### 
	
	def test_pop_response_1 (self):
		"""pop_response: present(only one)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3)]
		e = Event("Snow Ball", invs, resps)
		r = e.pop_response("R")
		self.assertEqual(r, Response("R",True,3))
		self.assertEqual(e.responses, [])
	
	def test_pop_response_2 (self):
		"""pop_response: present(first)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		r = e.pop_response("R")
		self.assertEqual(r, Response("R",True,3))
		self.assertEqual(e.responses, [Response("S",True,2), Response("T",False,0)])
	
	def test_pop_response_3 (self):
		"""pop_response: present(middle)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		r = e.pop_response("S")
		self.assertEqual(r, Response("S",True,2))
		self.assertEqual(e.responses, [Response("R",True,3), Response("T",False,0)])
	
	def test_pop_response_4 (self):
		"""pop_response: present(end)."""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		r = e.pop_response("T")
		self.assertEqual(r, Response("T",False,0))
		self.assertEqual(e.responses, [Response("R",True,3), Response("S",True,2)])
	
	def test_pop_response_5 (self):
		"""pop_response: not found (raises LookupError)"""
		invs = [Invitation("R",3),Invitation("S",5),Invitation("T",1)]
		resps = [Response("R",True,3), Response("S",True,2), Response("T",False,0)]
		e = Event("Snow Ball", invs, resps)
		try:
			r = e.pop_response("Waldo")
			self.fail("should have raised LookupError, because there's no Waldo here.")
		except LookupError:
			pass
	
	def test_pop_response_6 (self):
		"""pop_response: empty list (raises LookupError)"""
		invs = []
		resps = []
		e = Event("Snow Ball", invs, resps)
		try:
			r = e.pop_response("Waldo")
			self.fail("should have raised LookupError, because there's no Waldo here in an empty list.")
		except LookupError:
			pass
	
	########################################################################### 
	
	def test_read_response_1 (self):
		"""read_response: no invitations, name not found."""
		e = Event("shindig", [],[])
		try:
			e.read_response(Response("Waldo",True,2))
			self.fail("should have raised InviteNotFoundError.")
		except InviteNotFoundError:
			pass
	
	def test_read_response_2 (self):
		"""read_response: some invitations present, but name not found."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[])
		try:
			e.read_response(Response("Waldo",True,2))
			self.fail("should have raised InviteNotFoundError.")
		except InviteNotFoundError:
			pass
	
	def test_read_response_3 (self):
		"""read_response: invitation found; saying no."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[])
		e.read_response(Response('a',False,0))
		self.assertEqual(e.responses, [Response('a',False,0)])
		
	def test_read_response_4 (self):
		"""read_response: invitation found; saying partial yes."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[])
		e.read_response(Response('a',True,6))
		self.assertEqual(e.responses, [Response('a',True,6)])
		
	def test_read_response_5 (self):
		"""read_response: invitation found; saying full yes."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[])
		e.read_response(Response('a',True,11))
		self.assertEqual(e.responses, [Response('a',True,11)])
		
	def test_read_response_6 (self):
		"""read_response: invitation found; bringing too many!"""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[])
		try:
			e.read_response(Response('a',True,100))
			self.fail("should have raised TooManyError")
		except TooManyError:
			pass
			
	def test_read_response_7 (self):
		"""read_response: adding response to beginning of list."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('b',True,7),Response('c',True,8)])
		e.read_response(Response('a',True,6))
		self.assertEqual(e.responses,[Response('a',True,6),Response('b',True,7),Response('c',True,8)])
	
	def test_read_response_8 (self):
		"""read_response: adding repsonse to middle of list."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('a',True,6),Response('c',True,8)])
		e.read_response(Response('b',True,7))
		self.assertEqual(e.responses,[Response('a',True,6),Response('b',True,7),Response('c',True,8)])
	
	def test_read_response_9 (self):
		"""read_response: adding response to end of list."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('a',True,6),Response('b',True,7)])
		e.read_response(Response('c',True,8))
		self.assertEqual(e.responses,[Response('a',True,6),Response('b',True,7),Response('c',True,8)])
	
	def test_read_response_10 (self):
		"""read_response: replacing response at beginning of list."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('a',True,6),Response('b',True,7),Response('c',True,8)])
		e.read_response(Response('a',False,0))
		self.assertEqual(e.responses,[Response('a',False,0),Response('b',True,7),Response('c',True,8)])
	
	def test_read_response_11 (self):
		"""read_response: replacing response at middle of list."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('a',True,6),Response('b',True,7),Response('c',True,8)])
		e.read_response(Response('b',True,11))
		self.assertEqual(e.responses,[Response('a',True,6),Response('b',True,11),Response('c',True,8)])
	
	def test_read_response_12 (self):
		"""read_response: replacing response at end of list."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('a',True,6),Response('b',True,7),Response('c',True,8)])
		e.read_response(Response('c',True,13))
		self.assertEqual(e.responses,[Response('a',True,6),Response('b',True,7),Response('c',True, 13)])
	
	def test_read_response_13 (self):
		"""read_response: replacing only response in list."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('a',True,6)])
		e.read_response(Response('a',False,0))
		self.assertEqual(e.responses,[Response('a',False,0)])
	
	def test_read_response_14 (self):
		"""read_response: check that invitation list is unmodified."""
		e = Event("shindig", [Invitation('a',11),Invitation('b',12),Invitation('c',13)],[Response('a',True,6),Response('b',True,7),Response('c',True,8)])
		e.read_response(Response('a',False,0))
		self.assertEqual(e.invites, [Invitation('a',11),Invitation('b',12),Invitation('c',13)])	
	
	########################################################################### 
	
	def test_count_attendees_1 (self):
		"""count_attendees: zero (no invitations)"""
		e = Event("test3", [],[])
		self.assertEqual(e.count_attendees(),0)
	
	def test_count_attendees_2 (self):
		"""count_attendees: zero (all said no)"""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3)],[Response("A",False,0),Response("B",False,0),Response("C",False,0)])
		self.assertEqual(e.count_attendees(),0)
	
	def test_count_attendees_3 (self):
		"""count_attendees: all said yes/fully."""
		e = Event("test3", [Invitation("A",10),Invitation("B",20),Invitation("C",30)],[Response("A",True,10),Response("B",True,20),Response("C",True,30)])
		self.assertEqual(e.count_attendees(),60)
	
	def test_count_attendees_4 (self):
		"""count_attendees: all said yes, some not full (e.g. 2 attending of 5 invited)"""
		e = Event("test3", [Invitation("A",10),Invitation("B",20),Invitation("C",30)],[Response("A",True,10),Response("B",True,15),Response("C",True,25)])
		self.assertEqual(e.count_attendees(),50)
	
	def test_count_attendees_5 (self):
		"""count_attendees: some haven't responded, others partial-yes."""
		e = Event("test3", [Invitation("A",10),Invitation("B",20),Invitation("C",30)],[Response("A",True,10),Response("C",True,4)])
		self.assertEqual(e.count_attendees(),14)
	
	########################################################################### 
	
	def test_count_rejections_1 (self):
		"""count_rejections: no responses yet."""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3)],[])
		self.assertEqual(e.count_rejections(),0)
	
	def test_count_rejections_2 (self):
		"""count_rejections: some responded, all responses were no's."""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3)],[Response("A",False,0),Response("C",False,0)])
		self.assertEqual(e.count_rejections(),4)
	
	def test_count_rejections_3 (self):
		"""count_rejections: some responded yes (partial) and others no."""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3)],[Response("A",False,0),Response("B",True,1),Response("C",False,0)])
		self.assertEqual(e.count_rejections(),5)
	
	def test_count_rejections_4 (self):
		"""count_rejections: all responded no"""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3)],[Response("A",False,0),Response("B",False,0),Response("C",False,0)])
		self.assertEqual(e.count_rejections(),6)
	
	def test_count_rejections_5 (self):
		"""count_rejections: all responded yes"""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3)],[Response("A",True,1),Response("B",True,2),Response("C",True,3)])
		self.assertEqual(e.count_rejections(),0)
	
	def test_count_rejections_6 (self):
		"""count_rejections: all responded, mixed num_attending answers."""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3)],[Response("A",False,0),Response("B",True,1),Response("C",True,3)])
		self.assertEqual(e.count_rejections(),2)
	
	def test_count_rejections_7 (self):
		"""count_rejections: some responded, mixed num_attending answers."""
		e = Event("test3", [Invitation("A",1),Invitation("B",2),Invitation("C",3),Invitation("D",50)],[Response("A",False,0),Response("B",True,1),Response("D",True,49)])
		self.assertEqual(e.count_rejections(),3)
	
	########################################################################### 
	
	def test_max_attendance_1 (self):
		"""max_attendance: zero."""
		e = Event("graduation",[],[])
		self.assertEqual(e.max_attendance(), 0)
	
	def test_max_attendance_2 (self):
		"""max_attendance: all have responded yes."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("B",True,10),Response("C",True,5),Response("D",True,7)])
		self.assertEqual(e.max_attendance(), 27)
	
	def test_max_attendance_3 (self):
		"""max_attendance: all have responded no."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",False,0),Response("B",False,0),Response("C",False,0),Response("D",False,0)])
		self.assertEqual(e.max_attendance(), 0)
	
	def test_max_attendance_4 (self):
		"""max_attendance: all have responded (various answers)."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("B",True,6),Response("C",False,0),Response("D",True,1)])
		self.assertEqual(e.max_attendance(), 12)
	def test_max_attendance_5 (self):
		"""max_attendance: some have yet to respond (all others are yes)"""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("D",True,3)])
		self.assertEqual(e.max_attendance(), 23)
	def test_max_attendance_6 (self):
		"""max_attendance: some have yet to respond (all others are no)"""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",False,0),Response("C",False,0)])
		self.assertEqual(e.max_attendance(), 17)
	
	########################################################################### 
	
	def test_count_pending_1 (self):
		"""count_pending: none."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("B",True,6),Response("C",False,0),Response("D",True,1)])
		self.assertEqual(e.count_pending(), 0)
	
	def test_count_pending_2 (self):
		"""count_pending: some pending."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("C",False,0)])
		self.assertEqual(e.count_pending(), 17)
	
	def test_count_pending_3 (self):
		"""count_pending: all pending."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [])
		self.assertEqual(e.count_pending(), 27)
	
	########################################################################### 
	
	def test_rescind_invitation_1 (self):
		"""rescind_invitation: just the only invitation."""
		e = Event("graduation",[Invitation("A",5)], [])
		e.rescind_invitation("A")
		self.assertEqual(e.invites, [])
		
	def test_rescind_invitation_2 (self):
		"""rescind_invitation: just invitation."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10)], [])
		e.rescind_invitation("A")
		self.assertEqual(e.invites, [Invitation("B",10)])
		
	def test_rescind_invitation_3 (self):
		"""rescind_invitation: invitation and partial-yes response."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("B",True,6),Response("C",True,3),Response("D",True,1)])
		e.rescind_invitation("C")
		self.assertEqual(e.invites, [Invitation("A",5),Invitation("B",10), Invitation("D",7)])
		self.assertEqual(e.responses, [Response("A",True,5),Response("B",True,6),Response("D",True,1)])
	
	def test_rescind_invitation_4 (self):
		"""rescind_invitation: invitation and full-yes response."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("B",True,6),Response("C",True,5),Response("D",True,1)])
		e.rescind_invitation("C")
		e.rescind_invitation("B")
		self.assertEqual(e.invites, [Invitation("A",5), Invitation("D",7)])
		self.assertEqual(e.responses, [Response("A",True,5), Response("D",True,1)])
	
	def test_rescind_invitation_5 (self):
		"""rescind_invitation: invitation and full-no response."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("B",True,6),Response("C",False,0),Response("D",True,1)])
		e.rescind_invitation("C")
		self.assertEqual(e.invites, [Invitation("A",5),Invitation("B",10), Invitation("D",7)])
		self.assertEqual(e.responses, [Response("A",True,5),Response("B",True,6),Response("D",True,1)])
	
	def test_rescind_invitation_6 (self):
		"""rescind_invitation: neither invitation nor response."""
		e = Event("graduation",[Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)], [Response("A",True,5),Response("B",True,6),Response("C",True,3),Response("D",True,1)])
		e.rescind_invitation("the phantom")
		# both unchanged.
		self.assertEqual(e.invites, [Invitation("A",5),Invitation("B",10),Invitation("C",5),Invitation("D",7)])
		self.assertEqual(e.responses, [Response("A",True,5),Response("B",True,6),Response("C",True,3),Response("D",True,1)])
	
    ############################################################################

	
# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		self.num_req = 0
		self.num_ec = 0
		# find all methods that begin with "test".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				# append regular tests
				# drop any digits from the end of str(func).
				dropnum = str(func)
				while dropnum[-1] in "1234567890":
					dropnum = dropnum[:-1]
				
				if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
					fs.append(AllTests(str(func)))
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))
		
#		print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test_extra_credit_".
			fs = []
			for w in wants:
				for func in AllTests.__dict__:
					if str(func).startswith("test_extra_credit_"+w):
						fs.append(AllTests(str(func)))
		
#			print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	this_file = __file__
	if dir==".":
		dir = os.getcwd()
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			if file==this_file:
				continue
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")
	
	if BATCH_MODE:
		print("BATCH MODE.\n")
		run_all()
		return
		
	else:
		want_all = len(sys.argv) <=2
		wants = []
		# remove batch_mode signifiers from want-candidates.
		want_candidates = sys.argv[2:]
		for i in range(len(want_candidates)-1,-1,-1):
			if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
				del want_candidates[i]
	
		# set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
		wants = []
		extra_credits = []
		if not want_all:
			for w in want_candidates:
				if w in REQUIRED_DEFNS:
					wants.append(w)
				elif w in SUB_DEFNS:
					wants.append(w)
				elif w in EXTRA_CREDIT_DEFNS:
					extra_credits.append(w)
				else:
					raise Exception("asked to limit testing to unknown function '%s'."%w)
		else:
			wants = REQUIRED_DEFNS + SUB_DEFNS
			extra_credits = EXTRA_CREDIT_DEFNS
		
		# now that we have parsed the function names to test, run this one file.	
		run_one(wants,extra_credits)	
		return
	return # should be unreachable!	

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):
	
	has_reqs = len(wants)>0
	has_ec   = len(extra_credits)>0
	
	# make sure they exist.
	passed1 = 0
	passed2 = 0
	tried1 = 0
	tried2 = 0
	
	# only run tests if needed.
	if has_reqs:
		print("\nRunning required definitions:")
		(tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
	if has_ec:
		print("\nRunning extra credit definitions:")
		(tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)
	
	# print output based on what we ran.
	if has_reqs and not has_ec:
		print("\n%d/%d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("\nScore based on test cases: %.2f/%d (%.2f*%d) " % (
																passed1*weight_required, 
																total_points_from_tests,
																passed1,
																weight_required
															 ))
	elif has_ec and not has_reqs:
		print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
	else: # has both, we assume.
		print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
		print("\nScore based on test cases: %.2f / %d ( %d * %.2f + %d * %.2f) " % (
																passed1*weight_required+passed2*weight_extra_credit, 
																total_points_from_tests,
																passed1,
																weight_required,
																passed2,
																weight_extra_credit
															 ))
	if CURRENTLY_GRADING:
		print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
		filenames = files_list(sys.argv[1])
		#print(filenames)
		
		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS
		
		results = []
		for filename in filenames:
			print(" Batching on : " +filename)
			# I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
			lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()
			
			# delay of shame...
			time.sleep(DELAY_OF_SHAME)
			
			name = os.path.basename(lines[-1])
			stuff =lines[-2].split(" ")[1:-1]
			print("STUFF: ",stuff, "LINES: ", lines)
			(passed_req, tried_req, passed_ec, tried_ec) = stuff
			results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
			continue
		
		print("\n\n\nGRAND RESULTS:\n")
		
			
		for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req).strip()
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible, 
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))
# only used for batch mode.
def run_all_orig():
		filenames = files_list(sys.argv[1])
		#print(filenames)
		
		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS
		
		results = []
		for filename in filenames:
			# wipe out all definitions between users.
			for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
				globals()[fn] = decoy(fn)
				fn = decoy(fn)
			try:
				name = os.path.basename(filename)
				print("\n\n\nRUNNING: "+name)
				(tag_req, passed_req, tried_req) = run_file(filename,wants,False)
				(tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
				results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
				print(" ###### ", results)
			except SyntaxError as e:
				tag = filename+"_SYNTAX_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except NameError as e:
				tag =filename+"_Name_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ValueError as e:
				tag = filename+"_VALUE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except TypeError as e:
				tag = filename+"_TYPE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ImportError as e:
				tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except Exception as e:
				tag = filename+str(e.__reduce__()[0])
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
		
# 			try:
# 				print("\n |||||||||| scrupe: "+str(scruples))
# 			except Exception as e:
# 				print("NO SCRUPE.",e)
# 			scruples = None
		
		print("\n\n\nGRAND RESULTS:\n")
		for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req)
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible, 
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))

def try_copy(filename1, filename2, numTries):
	have_copy = False
	i = 0
	while (not have_copy) and (i < numTries):
		try:
			# move the student's code to a valid file.
			shutil.copy(filename1,filename2)
			
			# wait for file I/O to catch up...
			if(not wait_for_access(filename2, numTries)):
				return False
				
			have_copy = True
		except PermissionError:
			print("Trying to copy "+filename1+", may be locked...")
			i += 1
			time.sleep(1)
		except BaseException as e:
			print("\n\n\n\n\n\ntry-copy saw: "+e)
	
	if(i == numTries):
		return False
	return True

def try_remove(filename, numTries):
	removed = False
	i = 0
	while os.path.exists(filename) and (not removed) and (i < numTries):
		try:
			os.remove(filename)
			removed = True
		except OSError:
			print("Trying to remove "+filename+", may be locked...")
			i += 1
			time.sleep(1)
	if(i == numTries):
		return False
	return True

def wait_for_access(filename, numTries):
	i = 0
	while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
		print("Waiting for access to "+filename+", may be locked...")
		time.sleep(1)
		i += 1
	if(i == numTries):
		return False
	return True

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
	if wants==None:
		wants = []
	
	# move the student's code to a valid file.
	if(not try_copy(filename,"student.py", 5)):
		print("Failed to copy " + filename + " to student.py.")
		quit()
		
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import importlib
	count = 0
	while True:
		try:
# 			print("\n\n\nbegin attempt:")
			while True:
				try:
					f = open("student.py","a")
					f.close()
					break
				except:
					pass
# 			print ("\n\nSUCCESS!")
				
			import student
			importlib.reload(student)
			break
		except ImportError as e:
			print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
			time.sleep(0.5)
			while not os.path.exists("student.py"):
				time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			print("SyntaxError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_SYNTAX_ERROR",None, None, None)
		except NameError as e:
			print("NameError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return((filename+"_Name_ERROR",0,1))	
		except ValueError as e:
			print("ValueError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			print("TypeError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_TYPE_ERROR",0,1)
		except ImportError as e:			
			print("ImportError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details or try again")
			return((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
		except Exception as e:
			print("Exception in loading"+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+str(e.__reduce__()[0]),0,1)
	
	# make a global for each expected definition.
	for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			if fn in wants:
				print("\nNO DEFINITION FOR '%s'." % fn)	
	
	if not checking_ec:
		# create an object that can run tests.
		runner = unittest.TextTestRunner()
	
		# define the suite of tests that should be run.
		suite = TheTestSuite(wants)
	
	
		# let the runner run the suite of tests.
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		# print(ans)
	
	else:
		# do the same for the extra credit.
		runner = unittest.TextTestRunner()
		suite = TheExtraCreditTestSuite(wants)
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		#print(ans)
	
	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	if(not try_remove("student.py", 5)):
		print("Failed to remove " + filename + " to student.py.")
	
	tag = ".".join(filename.split(".")[:-1])
	
	
	return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
		# this can accept any kind/amount of args, and will print a helpful message.
		def failyfail(*args, **kwargs):
			return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
		return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()