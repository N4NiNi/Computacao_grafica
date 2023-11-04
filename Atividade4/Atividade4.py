

import numpy as np
from PIL import Image, ImageDraw

class ObjViewer:
    def __init__(self, filename):
        self.reader = ObjReader(filename)

    def generate_image(self, width, height, output_filename):
        self.reader.read()
        vertices = self.reader.get_vertices()
        faces = self.reader.get_faces()
        

        # Criar uma imagem em branco
        img = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(img)

        # Escala e translada os vértices para ajustar à imagem
        scale = min(width, height)
        for i in range(len(vertices)):
            x, y, z = vertices[i]
            x = int((x + 13) * 0.05 * scale)
            y = int((1 - (y + 0.5) * 0.05) * scale)
            vertices[i] = (x, y)

        face_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'orange']

        # Desenhar as faces
        for face in faces:
            points = [vertices[int(vertex.split('/')[0]) - 1] for vertex in face]
            color = face_colors[i % len(face_colors)]
            draw.polygon(points, outline='black', fill=color)

        # Salvar a imagem
        img.save(output_filename)

class ObjReader:

  def __init__(self, filename):
    
    """
    Inicia classe para ler o objeto.

    Args:
        filename: O caminho para o arquivo OBJ.

    """
    self.filename = filename
    self.vertices = None
    self.faces = None

  def read(self):
    """
    Função que lê o arquivo .obj e guarda os valores das faces e vertice do arquivo.

    """
    with open(self.filename) as f:
      lines = f.readlines()

    self.vertices = []
    self.faces = []

    for line in lines:
      line = line.strip()

      if line.startswith("v "):
        x, y, z = line.split()[1:]
        self.vertices.append([float(x), float(y), float(z)])

      elif line.startswith("f "):
        face = line.split()[1:]
        self.faces.append(face)

  def get_vertices(self):
    
    """
    Lê um arquivo OBJ e retorna os vertices e faces do objeto.

    Args:

    Returns:
        vertices: Uma lista os vertices do objeto.
    """
    return self.vertices

  def get_faces(self):
    """
    Lê um arquivo OBJ e retorna os vertices e faces do objeto.

    Args:

    Returns:
        faces: Uma lista com as faces do objeto.
    """
    return self.faces


if __name__ == "__main__":
  reader = ObjReader("obj\Rubik\Robik.obj")
  reader.read()
  print(reader.get_vertices())
  print(reader.get_faces())

  obj_viewer = ObjViewer('obj\Rubik\Robik.obj')
  obj_viewer.generate_image(800, 600, 'output.png')


