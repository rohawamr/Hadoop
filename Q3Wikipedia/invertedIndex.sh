#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file map_inverted_index.py reduce_inverted_index.py -mapper map_inverted_index.py -reducer reduce_inverted_index.py
