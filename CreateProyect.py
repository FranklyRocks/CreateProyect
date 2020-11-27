from distutils.dir_util import copy_tree
import sys

templatesDir = "./proyect_templates/"
templateName = sys.argv[1]

proyectsDir = "./"
proyectName = sys.argv[2]

copy_tree(templatesDir + templateName, proyectsDir + proyectName)
