import cv2 as cv

class CropLayer(object):
    def __init__(self, params, blobs):
        self.xstart = 0
        self.xend = 0
        self.ystart = 0
        self.yend = 0

    def getMemoryShapes(self, inputs):
        inputShape, targetShape = inputs[0], inputs[1]
        batchSize, numChannels = inputShape[0], inputShape[1]
        height, width = targetShape[2], targetShape[3]

        self.ystart = (inputShape[2] - targetShape[2]) // 2
        self.xstart = (inputShape[3] - targetShape[3]) // 2
        self.yend = self.ystart + height
        self.xend = self.xstart + width
        return [[batchSize, numChannels, height, width]]

    def forward(self, inputs):
        return [inputs[0][:,:,self.ystart:self.yend,self.xstart:self.xend]]

cv.dnn_registerLayer('Crop', CropLayer)

# Load the model.
net = cv.dnn.readNet("models/hed/deploy.prototxt", "models/hed/hed_pretrained_bsds.caffemodel")

kWinName = 'Holistically-Nested Edge Detection'
cv.namedWindow('Input', cv.WINDOW_AUTOSIZE)
cv.namedWindow(kWinName, cv.WINDOW_AUTOSIZE)

frame = cv.imread("images/input.jpg")
cv.imshow('Input', frame)

inp = cv.dnn.blobFromImage(frame, scalefactor=1.0, size=(500, 500),
                           mean=(104.00698793, 116.66876762, 122.67891434),
                           swapRB=False, crop=False)
net.setInput(inp)
out = net.forward()
out = out[0, 0]
out = cv.resize(out, (frame.shape[1], frame.shape[0]))

cv.imwrite("images/hed.jpg", out*255)
cv.imshow(kWinName, out)

# print("Shape of input:", frame.shape)
# print("Shape of output:", out.shape)
# print(out)
cv.waitKey(0)

