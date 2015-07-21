import os
from termcolor import colored

invalid = 'Invalid command'

cases = [
  ('db coll find | a 1, b 2', 'db.coll.find({"a": 1, "b": 2});'),
  ('db coll find | a 1, b 2 | c 3', 'db.coll.find({"a": 1, "b": 2}, {"c": 3});'),
  ('db coll find | a b 1, c 2', 'db.coll.find({"a": {"b": 1}, "c": 2});'),
  ('db coll find | a [a 1, b 2 ; c 3], d 4', 'db.coll.find({"a": [{"a": 1, "b": 2}, {"c": 3}], "d": 4});'),
  ('db coll find | "a" | 1 | [1 ; 2 ; 3]', 'db.coll.find("a", 1, [1, 2, 3]);'),
  ('db coll find | a 1, c => d => b 1, c 2', 'db.coll.find({"a": 1, "c": {"d": {"b": 1, "c": 2}}});'),
  ('db coll find | c => d => b 1, c 2, a 1', 'db.coll.find({"c": {"d": {"b": 1, "c": 2, "a": 1}}});'),
  ('db coll find | [e 5, a => b => c 2, d 3 ; f 6]', 'db.coll.find([{"e": 5, "a": {"b": {"c": 2, "d": 3}}}, {"f": 6}]);'),
  ('db coll find | {} | a {} | [1 ; {}]', 'db.coll.find({}, {"a": {}}, [1, {}]);'),
  ('db coll find | \$or [b \$in [2;3;"string"]; a 5]', 'db.coll.find({"$or": [{"b": {"$in": [2, 3, "string"]}}, {"a": 5}]});'), 
  ('db coll find | "a b" 1', 'db.coll.find({"a b": 1});'),
  ('db coll find | a "yay monquee"', 'db.coll.find({"a": "yay monquee"});'),
  ('db coll find | > 5, < 5, >= 5, <= 5, = 5, != 5', 'db.coll.find({"$gt": 5, "$lt": 5, "$gte": 5, "$lte": 5, "$eq": 5, "$ne": 5});'),
  ('db coll find | a=>b=>c 1', 'db.coll.find({"a": {"b": {"c": 1}}});'),
  ('db coll find | a.b 1', 'db.coll.find({"a.b": 1});'),
  ('db people find | | name 1', 'db.people.find({}, {"name": 1});'),
  ('use mydb', 'use mydb;'),
  ('foo bar baz', invalid)
]

for case in cases:
	cmd = 'echo "' + case[0].replace('"', '\\"') +  '" | ./mongo'
	output = os.popen(cmd).read()
	passed = output[:-1] == case[1] # trim newline
	result = ('PASSED' if passed else 'FAILED') + ': ' + case[0] + (("\nExpected:\t" + case[1] + "\nReceived:\t"+output) if not passed else '')
	print colored(result, 'green' if passed else 'red')
