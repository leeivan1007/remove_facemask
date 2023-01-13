# Download repositories
git clone https://github.com/JiahuiYu/generative_inpainting
git clone https://github.com/JiahuiYu/neuralgym


conda create --name gi python=3.8
conda activate gi
pip install tensorflow-gpu==2.7

# Test GPU -> tf.test.is_gpu_available()

conda install -c anaconda cudatoolkit
conda install -c anaconda cudnn


tf_upgrade_v2 --intree generative_inpainting-master --outtree generative_inpainting
tf_upgrade_v2 --intree neuralgym-master --outtree neuralgym

# Install packages
pip install opencv-python
pip install pyyaml
pip install tf-slim
pip install pillow