import open3d as o3d
import numpy as np
import trimesh

class ModelGenerator:
    def __init__(self):
        pass

    def generate_cube(self, size=1.0):
        """Generate a cube mesh"""
        mesh = o3d.geometry.TriangleMesh.create_box(width=size, height=size, depth=size)
        mesh.compute_vertex_normals()
        return mesh

    def generate_sphere(self, radius=1.0):
        """Generate a sphere mesh"""
        mesh = o3d.geometry.TriangleMesh.create_sphere(radius=radius)
        mesh.compute_vertex_normals()
        return mesh

    def generate_custom_mesh(self):
        """Generate a simple custom triangular mesh"""
        vertices = np.array([
            [0, 0, 0], [1, 0, 0], [0.5, 1, 0], 
            [0.5, 0.5, 1]  # Extra vertex for 3D shape
        ])
        faces = np.array([
            [0, 1, 2], [0, 2, 3], [1, 2, 3], [0, 1, 3]
        ])
        
        mesh = o3d.geometry.TriangleMesh()
        mesh.vertices = o3d.utility.Vector3dVector(vertices)
        mesh.triangles = o3d.utility.Vector3iVector(faces)
        mesh.compute_vertex_normals()
        return mesh

    def export_mesh(self, mesh, filename="model.obj"):
        """Export the generated mesh to an OBJ or STL file"""
        o3d.io.write_triangle_mesh(filename, mesh)
        print(f"Mesh saved as {filename}")

    def visualize_mesh(self, mesh):
        """Visualize the 3D model"""
        o3d.visualization.draw_geometries([mesh])

if __name__ == "__main__":
    generator = ModelGenerator()

    # Choose a model to generate
    cube = generator.generate_cube(2.0)
    sphere = generator.generate_sphere(1.5)
    custom_mesh = generator.generate_custom_mesh()

    # Export models
    generator.export_mesh(cube, "cube.obj")
    generator.export_mesh(sphere, "sphere.obj")
    generator.export_mesh(custom_mesh, "custom_mesh.obj")

    # Visualize models
    generator.visualize_mesh(cube)
    generator.visualize_mesh(sphere)
    generator.visualize_mesh(custom_mesh)
