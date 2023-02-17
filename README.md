# vln-demo

This is a demo for adding 3D people in [**MatterPort3D Simlulator**](https://github.com/peteanderson80/Matterport3DSimulator)

## How to run:
### 1. Create conda environment

```
conda create --name vln_demo python=3.8
conda activate vln_demo
```

### 2. install the following packages in your environnement:
```bash
pip install opencv-python
pip install matplotlib
pip install numpy
pip install pandas

```

### 3. Demo
**We offer dataset in [dataset](demo_dataset) for visualization of three different trajectories, and you can download our 40 categories of 360 degrees generated human motions (46G) from [**google drive**](https://drive.google.com/file/d/1P1xKbzquhBtDEmoR1qOC8BPKi_nXk1LV/view?usp=sharing), unzip the human folder under ``/vln-demo/360degree_human``**

Without downloading 360 degrees of human motions, you can also run a simplified version of our demo (variation of action is limited this way), run [demo.ipynb](demo.ipynb) and choose one path for demo!

### 4. Add 3D human to MatterPort 3D
**you need to download RGB image data from [here](https://github.com/peteanderson80/Matterport3DSimulator) and place under ``/vln-demo/data`` and ``/vln-demo/data_test``**
1. add 3D human in one scan, can check the results via [read_img.ipynb](read_img.ipynb)
```bash
python combine_all.py --mode run_single --scan 1LXtFkjw3qL

```

2. add 3D human in one scan, can check the results via [read_img.ipynb](read_img.ipynb)
```bash
python combine_all.py --mode run_all

```
