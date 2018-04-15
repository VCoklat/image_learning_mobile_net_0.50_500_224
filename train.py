#!/usr/bin/python

import os, sys
#untuk mengakses os sisem

from datetime import datetime
#untuk mengambil waktu

start=datetime.now()
#memulai waktu untuk menghitung lama training

for i in range(1,11): #looping 1-11 karena ada 10 grup
   os.chdir('/home/snewbie/Downloads/mobile_net_0.50_500_224/tf'+str(i)) #berpindah ke folder testing
   os.system('python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture=mobilenet_0.50_224 \
  --image_dir=../../training_image/tf'+str(i)+'/floor') #menjalankan perinta retrain.py di dalam folder script dengan file bottleneck training di tf_file/bottlenecks dengan 500 training model di tf_file/models/ dan hasilnya disimpan sebagai summary yang bisa diakses di tf_files/training summaries. Grafik training disimpan di tf_files/retrained_graph dan output_labelnya disimpan di tf_files/retrained_label dengan arsitektur mobile_net_0.50_224 untuk menentukan file yang didownload dan sumber imagenya di luar floor

print datetime.now()-start
#selesai training print waktu

