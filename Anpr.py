import cv2
# from cv2  import dnn_superres
import torch
from skimage.io import imread_collection
from ultralytics import YOLO
from cv2 import dnn_superres
yolo = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
my_model = YOLO('weights_segment/best.pt')
sr = dnn_superres.DnnSuperResImpl_create()
path = 'EDSR_x4.pb'
sr.readModel(path)
sr.setModel('edsr', 4)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$Devloped by sobttm
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@start_detaction_@@@@@@@@@@@@@@@@@@@@@@@@@@@
def detection():
    #++++++++++++++++++++load_custom_model_weights++++++++++++++++++++ 
    # yolo = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

    # print(yolo)

    #++++++++++++++++++++Read_image_from_directory+++++++++++++++++++++++++
    #your path
    # col_dir = f"2000img_first/{img_data}"
    col_dir = 'images/*.jpg'
    #+++++++++++creating a collection with the available images+++++++++++++
    col = imread_collection(col_dir)
    print(col)

    #+++++++++++++++++detect_position_plr_&&_croping_image_&&_save_to_res_directory++++++
    count=0
    for i in col:
        # print(i)
        img = i
        results = yolo(img)
        print("results is ")
        print(results)
        cordinates = results.xyxy[0][:,:-1]
        df = results.pandas().xyxy[0]
        frame = img
        print(df)
        # try:
        plate = frame[int(df.iloc[0]['ymin']) : int(df.iloc[0]['ymax']), int (df.iloc[0]['xmin']) : int (df.iloc[0]['xmax'])]
        # Save the cropped image
        # print(f"res/{i}")
        cv2.imwrite(col.files[count], plate)
        count=count+1
        # except:
        #     count=count+1
    return f"res/"

#////////just for test
# img_data = "2005.jpg"
# resulttest = detection(img_data)
# print(resulttest)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@End_detaction_@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@start_Segmentaion_@@@@@@@@@@@@@@@@@@@@@@@@@@@
def segmentaion():

    #+++++++++++++++++++Mask_for_beter_resoulation+++++++++++++++++++++++++
    # sr = dnn_superres.DnnSuperResImpl_create()
    #++++++++++++++++++++++++ read the model+++++++++++++++++++++++++++++++
    # path = 'EDSR_x4.pb'
    # sr.readModel(path)
    #++++++++++++++++++++++set the model and scale+++++++++++++++++++++++++
    # sr.setModel('edsr', 4)
    #++++++++++++++++++++++load the image+++++++++++++++++++++++++++++++++
    col_dir = 'images/*.jpg'
    col = imread_collection(col_dir)
    count = 0 
    all_dicts = {}
    for i in col:
        image = i
        upscaled = sr.upsample(image)
        cv2.imwrite(col.files[count], upscaled)
        
        res = my_model(col.files[count])
        names = my_model.names
        clas_names = []
        for r in res : 
            crd = r.boxes.xyxy
            for c in r.boxes.cls:
                clas_names.append(names[int(c)])

        dictt={}
        coordinates = crd.tolist()
        for i in range(len(clas_names)):
            dictt[clas_names[i]] = coordinates[i][0] 

        print(dictt)
        sorted_last = {k: v for k, v in sorted(dictt.items(), key=lambda item: item[1])}
        all_dicts[col.files[count]] = sorted_last 
        count = count+1

    return all_dicts      

            
                    






        





    # image = cv2.imread(f'{col}')
    # print(f'{col}')
    # # print(image)
    # upscaled = sr.upsample(image)
    # cv2.imwrite(f'upscaled/upscaled_test_{col}', upscaled)
    # print("ysss")
    # #++++++++++++++End_Mask++++++++++++++++++++++++++++++++++++++++++++++++
    # #++++++++++++++start_segment+++++++++++++++++++++++++++++++++++++++++++
    # my_model = YOLO('weights_segment/best.pt')
    # res = my_model(f'upscaled/upscaled_test_{col}')
    # names = my_model.names

    # clas_names = []
    # for r in res : 
    #     crd = r.boxes.xyxy
    #     for c in r.boxes.cls:
    #         clas_names.append(names[int(c)])
             
    #            # print(names[int(c)])


    # dictt={}
    # coordinates = crd.tolist()
    # for i in range(len(clas_names)):
    #     dictt[clas_names[i]] = coordinates[i][0]  


    # print(dictt)
    # sorted_last = {k: v for k, v in sorted(dictt.items(), key=lambda item: item[1])}
    # return sorted_last 
             



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@End_Segmentaion_@@@@@@@@@@@@@@@@@@@@@@@@@@@

# img_data = "upscaled_test_2_png.rf.cbdfee53c5aa31eceb757463687c93be(1)"
# resulttest = detection(img_data)
# print(segmentaion(resulttest))

#detection()
# my_model = YOLO('weights_segment/best.pt')
# print(segmentaion())