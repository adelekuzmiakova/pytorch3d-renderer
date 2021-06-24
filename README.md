## Medium article

[Checkout](https://adelekuzmiakova.medium.com/how-to-render-3d-files-using-pytorch3d-ef9de72483f8?source=friends_link&sk=d89816e7e6f338dfc68da836757e149d) the Medium walkthrough 👋 on how to render 3D `.obj` meshes from various viewpoints to create 2D images.

![Alt text](assets/medium.png?raw=true "Title")

[Read more](https://adelekuzmiakova.medium.com/how-to-render-3d-files-using-pytorch3d-ef9de72483f8?source=friends_link&sk=d89816e7e6f338dfc68da836757e149d)

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

This takes a 3D `.obj` file and renders it to create 2D images from multiple viewpoints based on parameters specified in `params.json`.  The resulting images are then saved in `out/` directory. The `.json` parameters include:

`image_size` is a size of an actual 2D output image. The smaller the size, the more pixelated the image will appear. Try 512 or 1024 to get crisp images but, by the same token, the code will take longer to run.\
`camera_dist` refers to the distance between the camera and the object.\
`elevation` is a **list** of elevation values and basically tell us from how high we are looking at the object. **Elevation refers to the angle between the vector from the object to the camera and the horizontal plane y=0 (plane xz).**\
`azim_angle` is a **list** of azimuth angle values and basically tell us from which side (e.g. left size, right side, front view, back view, etc.) we are looking at the object. What's azimuth angle? **Let's say you have a vector from the object to the camera and you project it onto a horizontal plane y=0. The azimuth angle is then the angle between the projected vector and a reference vector at (0,0,1) on the reference plane (horizontal plane).** [Checkout](https://www.celestis.com/resources/faq/what-are-the-azimuth-and-elevation-of-a-satellite/) this illustration.\
`obj_filename` is a path to the `.obj` file you want to render.

&nbsp;

### a) 3D cow mesh example


`.json` parameters:

```json
{
"image_size": 256,
"camera_dist": 3,   
"elevation": [0, 90, 180],
"azim_angle": [0, 60, 90, 180, 270],
"obj_filename": "data/cow_mesh/cow.obj"
}
```

&nbsp;

Rendered results (also stored in `out` directory):
![Alt text](assets/cowmesh.png?raw=true "Title")

&nbsp;

### b) 3D capsule mesh example

[Data source](http://paulbourke.net/dataformats/obj/minobj.html)

`.json` parameters:

```json
{
"image_size": 256,
"camera_dist": 3,   
"elevation": [0, 90, 180],
"azim_angle": [0, 60, 90, 180, 270],
"obj_filename": "data/capsule/capsule.obj"
}
```

### c) 2D rooster mesh example

[Data source](https://free3d.com/3d-model/low-poly-rooster-31363.html)

**IMPORTANT:** Pre-process the mesh to make sure that 1 of the 3 coordinates (x, y, or z) is a constant. In this case, `process_rooster_mesh.py` sets the z-coordinate to 0. 

```bash
python -m process_rooster_mesh
```


`.json` parameters:

```json
{
"image_size": 1024,
"camera_dist": 10,   
"elevation": [0, 90, 180],
"azim_angle": [0, 60, 90, 180, 270],
"obj_filename": "data/rooster/rooster_1.0.1.obj"
}
```
Blender visualization:
![Alt text](assets/rooster_blender.png?raw=true "Title")


Rendered results (also stored in `out` directory):
![Alt text](assets/rooster_rendered.png?raw=true "Title")
