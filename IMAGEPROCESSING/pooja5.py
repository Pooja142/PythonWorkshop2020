import cv2

img =["waterfall.jpg","waterfall2.jpg","waterfall3.jpg","waterfall4.jpg","waterfall5.jpg","waterfall6.jpg","waterfall7.jpg","waterfall8.jpg","waterfall9.jpg","waterfall10.jpg",1]

img1 = cv2.imread("waterfall.jpg",1)
print(img)
print(type(img))
print(img1.shape)
print(img.ndim)
print(img1.ndim)

cv2.imshow("pooja",img)
cv2.waitKey(2000)
cv2.destroyAllWindows 

resize_img = cv2.resize(img,(500,367))
cv2.imshow("newIMAGE",resize_img)
cv2.waitKey(2000)


'''for i in img:
	i=cv2.imread(i,1)
	r_img = cv2.resize(i,(int(i.shape[1]/2),int(i.shape[0]/2)))
	cv2.imshow("neWim",r_img)
	cv2.waitKey(3000)
	cv2.imwrite("neWim_resize.jpg",r_img)'''