#imagem 1
ffmpeg -i horses.png -c:v vp9 -b:v 0 -crf 10 horses_out1.mp4

ffmpeg -i horses_out1.mp4 horses_out1.png

ffmpeg -i horses.png -c:v vp9 -b:v 0 -crf 20 horses_out2.mp4

ffmpeg -i horses_out2.mp4 horses_out2.png

ffmpeg -i horses.png -c:v vp9 -b:v 0 -crf 30 horses_out3.mp4

ffmpeg -i horses_out3.mp4 horses_out3.png

ffmpeg -i horses.png -c:v vp9 -b:v 0 -crf 50 horses_out4.mp4

ffmpeg -i horses_out4.mp4 horses_out4.png

#Imagem 2

ffmpeg -i cars.png -c:v vp9 -b:v 0 -crf 10 cars_out1.mp4

ffmpeg -i cars_out1.mp4 cars_out1.png

ffmpeg -i cars.png -c:v vp9 -b:v 0 -crf 20 cars_out2.mp4

ffmpeg -i cars_out2.mp4 cars_out2.png

ffmpeg -i cars.png -c:v vp9 -b:v 0 -crf 30 cars_out3.mp4

ffmpeg -i cars_out3.mp4 cars_out3.png

ffmpeg -i cars.png -c:v vp9 -b:v 0 -crf 50 cars_out4.mp4

ffmpeg -i cars_out4.mp4 cars_out4.png

#Imagem 3
ffmpeg -i mountain.png -c:v vp9 -b:v 0 -crf 10 mountain_out1.mp4

ffmpeg -i mountain_out1.mp4 mountain_out1.png

ffmpeg -i mountain.png -c:v vp9 -b:v 0 -crf 20 mountain_out2.mp4

ffmpeg -i mountain_out2.mp4 mountain_out2.png

ffmpeg -i mountain.png -c:v vp9 -b:v 0 -crf 30 mountain_out3.mp4

ffmpeg -i mountain_out3.mp4 mountain_out3.png

ffmpeg -i mountain.png -c:v vp9 -b:v 0 -crf 50 mountain_out4.mp4

ffmpeg -i mountain_out4.mp4 mountain_out4.png



#JP222222222222222222222222222



ffmpeg -i horses.png -c:v jpeg2000 -qscale:v 100 horses_out1.jp2

ffmpeg -i horses_out1.jp2 horses_out1.png

ffmpeg -i horses.png -c:v jpeg2000 -qscale:v 1000 horses_out2.jp2

ffmpeg -i horses_out2.jp2 horses_out2.png

ffmpeg -i horses.png -c:v jpeg2000 -qscale:v 2000 horses_out3.jp2

ffmpeg -i horses_out3.jp2 horses_out3.png

ffmpeg -i horses.png -c:v jpeg2000 -qscale:v 5000 horses_out4.jp2

ffmpeg -i horses_out4.jp2 horses_out4.png



ffmpeg -i cars.png -c:v jpeg2000 -qscale:v 100 cars_out1.jp2

ffmpeg -i cars_out1.jp2 cars_out1.png

ffmpeg -i cars.png -c:v jpeg2000 -qscale:v 1000 cars_out2.jp2

ffmpeg -i cars_out2.jp2 cars_out2.png

ffmpeg -i cars.png -c:v jpeg2000 -qscale:v 2000 cars_out3.jp2

ffmpeg -i cars_out3.jp2 cars_out3.png

ffmpeg -i cars.png -c:v jpeg2000 -qscale:v 5000 cars_out4.jp2

ffmpeg -i cars_out4.jp2 cars_out4.png



ffmpeg -i mountain.png -c:v jpeg2000 -qscale:v 100 mountain_out1.jp2

ffmpeg -i mountain_out1.jp2 mountain_out1.png

ffmpeg -i mountain.png -c:v jpeg2000 -qscale:v 1000 mountain_out2.jp2

ffmpeg -i mountain_out2.jp2 mountain_out2.png

ffmpeg -i mountain.png -c:v jpeg2000 -qscale:v 2000 mountain_out3.jp2

ffmpeg -i mountain_out3.jp2 mountain_out3.png

ffmpeg -i mountain.png -c:v jpeg2000 -qscale:v 5000 mountain_out4.jp2

ffmpeg -i mountain_out4.jp2 mountain_out4.png



#libx265 codificador /hevc  libx265 codificador /HVEClibx265 codificador /HVEClibx265 codificador /HVEClibx265 codificador /HVEC

ffmpeg -i horses.png -c:v libx265 -b:v 0 -crf 10 horses_out1.hevc

ffmpeg -i horses_out1.hevc horses_out1.png

ffmpeg -i horses.png -c:v libx265 -b:v 0 -crf 20 horses_out2.hevc

ffmpeg -i horses_out2.hevc horses_out2.png

ffmpeg -i horses.png -c:v libx265 -b:v 0 -crf 30 horses_out3.hevc

ffmpeg -i horses_out3.hevc horses_out3.png

ffmpeg -i horses.png -c:v libx265 -b:v 0 -crf 50 horses_out4.hevc

ffmpeg -i horses_out4.hevc horses_out4.png


ffmpeg -i cars.png -c:v libx265 -b:v 0 -crf 10 cars_out1.hevc

ffmpeg -i cars_out1.hevc cars_out1.png

ffmpeg -i cars.png -c:v libx265 -b:v 0 -crf 20 cars_out2.hevc

ffmpeg -i cars_out2.hevc cars_out2.png

ffmpeg -i cars.png -c:v libx265 -b:v 0 -crf 30 cars_out3.hevc

ffmpeg -i cars_out3.hevc cars_out3.png

ffmpeg -i cars.png -c:v libx265 -b:v 0 -crf 50 cars_out4.hevc

ffmpeg -i cars_out4.hevc cars_out4.png


ffmpeg -i mountain.png -c:v libx265 -b:v 0 -crf 10 mountain_out1.hevc

ffmpeg -i mountain_out1.hevc mountain_out1.png

ffmpeg -i mountain.png -c:v libx265 -b:v 0 -crf 20 mountain_out2.hevc

ffmpeg -i mountain_out2.hevc mountain_out2.png

ffmpeg -i mountain.png -c:v libx265 -b:v 0 -crf 30 mountain_out3.hevc

ffmpeg -i mountain_out3.hevc mountain_out3.png

ffmpeg -i mountain.png -c:v libx265 -b:v 0 -crf 50 mountain_out4.hevc

ffmpeg -i mountain_out4.hevc mountain_out4.png

