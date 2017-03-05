from fc_lib import *
import opc
import time

if __name__ == '__main__':
    client = opc.Client('10.1.10.157:7890')
    cap = cv2.VideoCapture('bbb.mp4')
    while True:
            ret, img = cap.read()
            #print s
            #cv2.imshow('test',img)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
            #array = opencv_image_to_array(img) 
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            resized = cv2.resize(rgb, (32, 25)).tolist()
            flat =  [item for sublist in resized for item in sublist]
            array = fix_array(flat)
            ##client.put_pixels([[0,0,0]]*800)
            client.put_pixels(array)
            #client.put_pixels(array)
            time.sleep(1/60.)
    cap.release()
    cv2.destroyAllWindows()
