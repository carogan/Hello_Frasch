

if certainty_score > 0.6:
    messages = [
        {"role":"system", "content": "This is a chatbot by Alaiko that should recommend videos which target the logistics problems that are stated by the user. If a fitting video exists, you will receive a video link and a transcript of the video and should recommend the video to the user if his question is related to the topic."},
        {"role":"user","content": "The follwing is some information about the video you should recommend to the user. Here is the link: " + link + " and here is the transcript: " + transcript + ""},
        
    ]
else:
    messages = [
        {"role":"system", "content": "This is a chatbot by Alaiko that should recommend videos which target the logistics problems that are stated by the user. However, it seems like there is no fitting video right now so just tell the user to come back later."},
        {"role":"user","content": "It seems like there is no video which fits the problem very well. Here is some general information about Alaiko, more content will be added soon"},
        {"role":"assistant","content": f"Alaiko is the fastest growing fulfillment provider in Europe, specializing in e-commerce brands. Our mission is to help online shops offer their customers a seamless, first class experience with the ability to meet demand at scale. We put an end to manual, inconsistent and frustrating post-sale processes and help online shops create happy moments in e-commerce. Not only for their customers, but for themselves and everyone involved.Alaiko’s founders, Moritz and Gabriel, have known each other since college and have successfully established various businesses together. They felt the challenge of rapidly growing e-commerce brands with their own D2C brand and leveraged that experience when they founded Alaiko in April 2020"}
    ]


def generate_response(prompt):
    if prompt:
        messages.append({"role": "user", "content": prompt})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=messages,
            max_tokens = 2000,
            temperature = 0.1
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

    return reply