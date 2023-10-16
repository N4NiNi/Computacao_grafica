import math
from PIL import Image, ImageDraw
from vec2 import Vec2
from vec3 import Vec3
from vec4 import Vec4
from mat2 import Mat2
from mat3 import Mat3
from mat4 import Mat4
from color import Color

# Dimensões da imagem
width = 512
height = 512

# Cria uma imagem em branco
imagevec3 = Image.new("RGB", (width, height), (0, 0, 0))
imagevec4 = Image.new("RGBA", (width, height), (0, 0, 0, 255))

# Preenche a imagem com cores com base em coordenadas
for y in range(height):
    for x in range(width):
        # Cria uma cor com base nas coordenadas
        color_vec3 = Color(x / width, y / height, 0.5)
        color_vec4 = Vec4(x / width, y / height, 0.5, 1.0)

        # Converte as componentes de cor de ponto flutuante para 0-255
        r_vec3 = int(255.999 * color_vec3.x)
        g_vec3 = int(255.999 * color_vec3.y)
        b_vec3 = int(255.999 * color_vec3.z)

        r_vec4 = int(255.999 * color_vec4.x)
        g_vec4 = int(255.999 * color_vec4.y)
        b_vec4 = int(255.999 * color_vec4.z)
        a_vec4 = int(100 * color_vec4.a)

        # Define a cor do pixel na imagem
        imagevec3.putpixel((x, y), (r_vec3, g_vec3, b_vec3))
        imagevec4.putpixel((x, y), (r_vec4, g_vec4, b_vec4, a_vec4))

# Salva a imagem em um arquivo
imagevec3.save("output_vec3.png")
imagevec4.save("output_vec4.png")

image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)


# Exemplo usando mat3
# Carregue a imagem
image = Image.open("output_vec3.png")

# Dimensões da imagem
width, height = image.size

# Ângulo de rotação em radianos (por exemplo, 45 graus)
angle = math.radians(10)

# Matriz de rotação
cos_theta = math.cos(angle)
sin_theta = math.sin(angle)
rotation_matrix = Mat3(cos_theta, -sin_theta, 0, sin_theta, cos_theta, 0, 0, 0, 1)

# Crie uma nova imagem para a imagem transformada
new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(new_image)

# Transformação de rotação a cada pixel na imagem original
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        new_x = x * rotation_matrix.elements[0][0] + y * rotation_matrix.elements[0][1]
        new_y = x * rotation_matrix.elements[1][0] + y * rotation_matrix.elements[1][1]
        draw.point((int(new_x), int(new_y)), fill=pixel)

# Salve a imagem transformada
new_image.save("output_rotated.png")

