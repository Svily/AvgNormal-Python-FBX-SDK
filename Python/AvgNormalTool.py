from fbx import FbxNode

import FBXClass
import time

# replace it with your fbx file path
# path = "E:/Client/GrapicsLab/Clients/URPWater/URPWater/Assets/Prefab/Cube.fbx"
path = "E:/CubeTest.fbx"

def Start(path):
    fbxFile = FBXClass.FBX_Class(path)
    # print("Start AvgNormal....")
    # time_start = time.time()
    # fbxFile.AddVertColor(fbxFile.scene.GetRootNode())
    # fbxFile.AvgMeshNormal()
    # fbxFile.save()
    # time_end = time.time()
    # print("Done，Elapsed time:", time_end - time_start, "s")
    # fbxFile.scene.SetName("")
    # rootNode:FbxNode =
    print(fbxFile.scene.GetName())

Start(path)