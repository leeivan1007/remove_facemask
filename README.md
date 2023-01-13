# Remove_facemask

There project was built by me, Alex and 證壹. 

We want build the applications to remove facemask by AI algorithm. 

Our goal is make the perfect performance to comaper with Pixel algorithm.

But recording our resouces including time, devices and :moneybag:.

We decided to :sparkles:open source:sparkles: the whole project.

So If you have fun or intersting with our project. 

Please give the :star: we will appreciate it.:relaxed:

Also you can reference our [slide](https://docs.google.com/presentation/d/181eFUYPN-8y2xmDHlhNQoEO019DoeQBaOG5oyBcysgQ/edit?usp=sharing).

## Architecture

There are four parts you can enjoy with them.

1. Detection the face wearing the mask.

2. Remove the face.

3. Generate the blank

4. Generate the mask (Optional)

## 1. Detection the face wearing the mask.

## 2. Remove the face.

## 3. Generate the blank

We reference the project [generative_inpainting](https://github.com/JiahuiYu/generative_inpainting). 

But it's the older version. So it need some steps to update the version if you 

First off, you can install the project by gi_install.sh.

Second, becasue some issue with tf_upgrade_v2. You need to modify the code by yourself.

1. change the file [ inpaint_model.py ]
```
from tensorflow.contrib.framework.python.ops import arg_scope
-> from tf_slim import arg_scope
```
2. change the file [ inpaint_ops ]
```
from tensorflow.contrib.framework.python.ops import add_arg_scope
-> from tf_slim import arg_scope
```

Then install neuralgym
```
cd neuralgym
pip install -e .
cd ..
```
Download the weight from https://github.com/JiahuiYu/generative_inpainting#pretrained-models

Finally, you can test the code
```
python test.py --image examples/places2/case1_input.png --mask examples/places2/case1_mask.png --output examples/places2/case1_output_test.png --checkpoint_dir model_logs/release_places2_256_deepfill_v2
```
## 4. Generate the mask (Optional)

4.1 Imstall the gangealing
```
git clone https://github.com/wpeebles/gangealing.git
cd gangealing
conda env create -f environment.yml
conda activate gg
```

4.2 Set the environment parameters
```
export PYTHONPATH="${PYTHONPATH}:${PWD}"
```
4.3 Test the images
```
python prepare_data.py --input_is_lmdb --lsun_category cat --out data/lsun_cats --size 512 --max_images 10000
python applications/propagate_to_images.py --ckpt cat --real_data_path data/lsun_cats --real_size 512 --dset_indices 1922 2363 8558 7401 9750 7432 2105 53 1946
```
If it has a issue with "GLIBCXX_3.4.29" You can try the steps from ![here](https://stackoverflow.com/questions/65349875/where-can-i-find-glibcxx-3-4-29)

4.4 The the image with facemask
It prove the human face and the mask you can use them at images folder
```
python prepare_data.py --path folder_of_images --out data/my_new_dataset --pad [center/border/zero] --size S # build the data
python applications/propagate_to_images.py --ckpt celeba --real_data_path data/my_new_dataset --real_size 512 --dset_indices 0
```
Or if you feel complicate on this job, you can try this ![link](https://colab.research.google.com/drive/1JkUjhTjR8MyLxwarJjqnh836BICfocTu?usp=sharing) by office.

Just for fun for yourself! :raised_hands::fireworks::rocket: