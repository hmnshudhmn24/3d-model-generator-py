# 3D Model Generator

## Overview
This project generates 3D models using Python and Open3D. It supports creating procedural shapes like cubes, spheres, and custom meshes. The generated models can be exported as `.obj` files and visualized using Open3D.

## Features
- Generate **cubes, spheres, and custom 3D meshes**
- Export models in **OBJ format**
- **Visualize** models with Open3D
- Simple and extensible codebase

## Requirements
- Python 3.8+
- Open3D
- NumPy
- Trimesh

## Installation
1. Install dependencies:
   ```sh
   pip install open3d trimesh numpy
   ```
2. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/3d-model-generator.git
   cd 3d-model-generator
   ```

## Running the Program
Run the following command:
```sh
python 3d_model_generator.py
```

## How It Works
- Generates 3D models using Open3D's mesh creation tools.
- Provides **procedural generation** for cube, sphere, and a basic triangular mesh.
- Saves models as `.obj` files for use in Blender, MeshLab, and other 3D software.
