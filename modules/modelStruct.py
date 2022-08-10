import conf

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import losses

def createModel():
    mobileNetModel =  MobileNetV2(
        weights="imagenet",
        include_top=False,
        input_tensor=layers.Input(shape=conf.INPUT_IMAGE_SHAPE)
    )

    mobileNetModel_output = mobileNetModel.output

    pool_size = (conf.INPUT_IMAGE_SIZE[0]//32, conf.INPUT_IMAGE_SIZE[1]//32)
    mobileNetModel_output = layers.AveragePooling2D(pool_size)(mobileNetModel_output) # => output_shape = (32, 32)
    mobileNetModel_output = layers.Flatten(name="flatten")(mobileNetModel_output) # => output_shape = 1024
    mobileNetModel_output = layers.Dense(128, activation="relu")(mobileNetModel_output)
    mobileNetModel_output = layers.Dropout(0.5)(mobileNetModel_output)
    mobileNetModel_output = layers.Dense(2, activation="softmax")(mobileNetModel_output)

    model = Model(inputs=mobileNetModel.input, outputs=mobileNetModel_output)

    # https://keras.io/guides/transfer_learning/
    for layer in mobileNetModel.layers:
        layer.trainable = False

    model.compile(
        # Tính toán sự mất mát entropy chéo giữa các nhãn đúng và các nhãn được dự đoán.
        # https://keras.io/api/losses/probabilistic_losses/#binary_crossentropy-function
        loss = losses.BinaryCrossentropy(from_logits=False),  
        metrics=['accuracy'],

        optimizer = Adam(
            lr = conf.INIT_LR,
            decay = conf.INIT_LR / conf.EPOCHS
        ),
    )

    return model