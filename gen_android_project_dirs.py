# -*- coding: UTF-8 -*-

import os
import sys

package_root = sys.argv[1]
os.chdir(package_root)

package_template = {"common": ["util", "entity", "net"],
                    "data": ["entity", "db", "constant"],
                    "domain": ["cache", "request", "response"],
                    "presentation": ["app", "activity", "service", "broadcast", "adapter"]
                    }

for dir in package_template.keys():
    print(dir)
    os.chdir(package_root)
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    for sub in package_template[dir]:
        print(dir + "/" + sub)
        if not os.path.exists(sub):
            os.mkdir(sub)
