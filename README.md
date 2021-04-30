## Medium article

[Click here](https://adelekuzmiakova.medium.com/how-to-render-3d-files-using-pytorch3d-ef9de72483f8?source=friends_link&sk=d89816e7e6f338dfc68da836757e149d) for the Medium walkthrough on how to render `.obj` meshes from various viewpoints to create 2D images.

![Alt text](assets/medium_3.png?raw=true "Title")

## Setup your environment

```bash
conda env create -f environment.yml       # creates pytorch3d-renderer environment
conda activate pytorch3d-renderer         # activates the environment
conda deactivate                          # deactivates the environment
```




## Try out the demo

`render_demo.ipynb` is a Jupyter notebook that walks you through the entire rendering pipeline in PyTorch. The rendering parameters are specified in `params_demo.json` and can be modified there.

## Rendering code

The actual code is written in `render.py`:

```bash
python -m render
```

This takes a 3D `.obj` file and renders it to create 2D images from multiple viewpoints based on parameters specified in `params.json`.  These parameters include:

```json
{
"image_size": 256,
"camera_dist": 3,   
"elevation": [0, 90, 180],
"azim_angle": [0, 60, 90, 180, 270],
"obj_filename": "data/cow_mesh/cow.obj"
}
```
`image_size` is a size of an actual 2D output image. The smaller the size, the more pixelated the image will appear. Try 512 or 1024 to get crisp images but, by the same token, the code will take longer to run.\
`camera_dist` refers to the distance between the camera and the object.\
`elevation` is a **list** of elevation values and basically tell us from how high we are looking at the object. **Elevation refers to the angle between the vector from the object to the camera and the horizontal plane y=0 (plane xz).**\
`azim_angle` is a **list** of azimuth angle values and basically tell us from which side (e.g. left size, right side, front view, back view, etc.) we are looking at the object. What's azimuth angle? **Let's say you have a vector from the object to the camera and you project it onto a horizontal plane y=0. The azimuth angle is then the angle between the projected vector and a reference vector at (0,0,1) on the reference plane (horizontal plane).** [Click here](https://www.celestis.com/resources/faq/what-are-the-azimuth-and-elevation-of-a-satellite/) for another picture.\
`obj_filename` is a path to the obj file you want to render.


