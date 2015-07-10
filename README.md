
Trying to run Caffe on EC2

Now has complete instructions to configure an Ubunty EC2 g-instance up to have Caffee and ffmpeg which is enough to create deep dream inception videos.

See:
 * https://github.com/BVLC/caffe/wiki/Install-Caffe-on-EC2-from-scratch-(Ubuntu,-CUDA-7,-cuDNN)
 * http://rocknrollnerd.github.io/ml/2015/05/27/leopard-sofa.html
 * https://news.ycombinator.com/item?id=9749660
 * http://www.win-vector.com/blog/2015/06/neural-net-image-salad-again-with-code/
 
Should be good for applying:
 * https://github.com/google/deepdream
 * https://github.com/samim23/DeepDreamAnim

To use:
 *  Start an EC2 instance 
   * A g instance such as g2.8xlarge instance (about $2.60 per hour)
   * OS: Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-5189a661
   * Must go to instance details to make sure you have more storage (I used 64GB)
 *  Follow the many steps in steps.txt

![Example image](exampleImg.jpeg)