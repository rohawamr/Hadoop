#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file mapper2.py reducer2.py -mapper mapper2.py -reducer reducer2.py
