import boto.ec2
import sys
conn = boto.ec2.connect_to_region(sys.argv[1])
key_pair_list = conn.get_all_key_pairs()
def key_pair_check(keyname):
  for keypair in key_pair_list:
    if keypair.name == keyname:
      print "True"
key_pair_check(sys.argv[2])
