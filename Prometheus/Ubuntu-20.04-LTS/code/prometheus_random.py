#!/usr/bin/env python3
#
# Random stuff
#
##########################

import sys
import os
import random

base_dir="/var/lib/node_exporter/textfile_collector/"

##########################
#  Main
##########################
if __name__ == '__main__':

  #Test if base folder exist

  try:
    if not os.path.exists(base_dir):
      print("folder '" + base_dir + "' does not exist")
      sys.exit(1)
    else:
      prom_data  = "# HELP my_test_data_01 just some test data\n"
      prom_data += "# TYPE my_test_data_01 gauge\n"
      prom_data += "my_test_data_01 " + str(random.randint(1,100)) + "\n"   

      prom_data += "# HELP my_test_data_02 just some test data\n"
      prom_data += "# TYPE my_test_data_02 gauge\n"
      prom_data += "my_test_data_02 " + str(random.randint(1,100)) + "\n"

      prom_data += "# HELP my_test_data_03 just some test data\n"
      prom_data += "# TYPE my_test_data_03 gauge\n"
      prom_data += "my_test_data_03 " + str(random.randint(1,100)) + "\n" 

      f = open(base_dir + "/my_data.prom", 'w')
      f.write(prom_data)
      f.close() 

  except Exception as e:
    print("Exception {0}", e)
    sys.exit(1)
