import openai

openai.api_key = "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"

# Set your OpenAI API key
# api_key = "YOUR_API_KEY"
# openai.api_key = api_key

# Your input text
input_text = """

Last summer, my family and I visited Russia. Even though none of us could read Russian, we did not have any trouble in figuring our way out, all thanks to Google's real-time translation of Russian boards into English. This is just one of the several applications of neural networks. Neural networks form the base of deep learning, a subfield of machine learning where the algorithms are inspired by the structure of the human brain. Neural networks take in data, train themselves to recognize the patterns in this data, and then predict the outputs for a new set of similar data. Let's understand how this is done. Let's construct a neural network that differentiates between a square, circle, and triangle. Neural networks are made up of layers of neurons. These neurons are the core processing units of the network. First, we have the input layer which receives the input. The output layer predicts our final output. In between exist the hidden layers which perform most of the computations required by our network. Here's an image of a circle. This image is composed of 28 by 28 pixels, which make up for 784 pixels. Each pixel is fed as input to each neuron of the first layer. Neurons of one layer are connected to neurons of the next layer through channels. Each of these channels is assigned a numerical value known as weight. The inputs are multiplied to the corresponding weights and their sum is sent as input to the neurons in the hidden layer. Each of these neurons is associated with a numerical value called the bias, which is then added to the input sum. This value is then passed through a threshold function called the activation function. The result of the activation function determines if the particular neuron will get activated or not. An activated neuron transmits data to the neurons of the next layer over the channels. In this manner, the data is propagated through the network. This is called forward propagation. In the output layer, the neuron with the highest value fires and determines the output. The values are basically a probability. For example, here our neuron associated with square has the highest probability. Hence, that's the output predicted by the neural network. Of course, just by a look at it, we know our neural network has made a wrong prediction. But how does the network figure this out? Note that our network is yet to be trained. During this training process, along with the input, our network also has the output fed to it. The predicted output is compared against the actual output to realize the error in prediction. The magnitude of the error indicates how wrong we are, and the sign suggests if our predicted values are higher or lower than expected. The arrows here give an indication of the direction and magnitude of change to reduce the error. This information is then transferred backward through our network. This is known as backpropagation. Now, based on this information, the weights are adjusted. This cycle of forward propagation and backpropagation is iteratively performed with multiple inputs. This process continues until our weights are assigned such that the network can predict the shapes correctly in most of the cases. This brings our training process to an end. You might wonder how long this training process takes. Honestly, neural networks may take hours or even months to train. But time is a reasonable trade-off when compared to its scope. Let us look at some of the prime applications of neural networks. Facial recognition. Cameras on smartphones these days can estimate the age of the person based on their facial features. This is neural networks at play, first differentiating the face from the background and then correlating the lines and spots on your face to a possible age. Forecasting. Neural networks are trained to understand the patterns and detect the possibility of rainfall or a rise in stock prices with high accuracy. Music composition. Neural networks can even learn patterns in music and train itself enough to compose a fresh tune. So, here's a question for you. Which of the following statements does not hold true? A. Activation functions are threshold functions. B. Error is calculated at each layer of the neural network. C. Both forward and back propagation take place during the training process of a neural network. D. Most of the data processing is carried out in the hidden layers. Leave your answers in the comment section below. Three of you stand a chance to win Amazon vouchers. So, don't miss it. With deep learning and neural networks, we are still taking baby steps. The growth in this field has been foreseen by the big names. Companies such as Google, Amazon, and NVIDIA have invested in developing products such as libraries, predictive models, and intuitive GPUs that support the implementation of neural networks. The question dividing the visionaries is on the reach of neural networks. To what extent can we replicate the human brain? We'd have to wait a few more years to give a definite answer. But, if you enjoyed this video, it would only take a few seconds to like and share it. Also, if you haven't yet, do subscribe to our channel and hit the bell icon, as we have a lot more exciting videos coming up. Fun learning till then!
"""

def generate_flashcards(text):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Create 12 flashcards for memorization based on the following text:\n\n{text}\n\nFlashcard 1:\n1. ",
        max_tokens=500,
        n=1  # Generate one response with 12 flashcards
    )

    # Extract the text from the response
    response_text = response.choices[0].text.strip()

    # Split the response text into individual flashcards
    flashcards = response_text.split("\n")

    return flashcards








flashcards = generate_flashcards(input_text)
print(len(flashcards))


print(flashcards)

# # Print the flashcards
# for i, card in enumerate(flashcards):
#     print(f"Card {i + 1}:\n\n{card}\n")