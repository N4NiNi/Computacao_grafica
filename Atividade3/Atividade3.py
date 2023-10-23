

import numpy as np

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
  reader = ObjReader("obj\Wolf_obj.obj")
  reader.read()
  print(reader.get_vertices())
  print(reader.get_faces())

