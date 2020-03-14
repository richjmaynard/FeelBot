What is FeelBot?

FeelBot is a collective of internet-connected robots that all feel the same thing at the same time. FeelBot can feel happy, sad, anxious, angry...
Some FeelBots have faces that move, some are based on led displays and others show their emotions through their body language. Some dance, some sing and some sit quietly and just listen.

How does it work?

Every FeelBot connects to the internet and regulates its feelings based on a central server.
The server speaks MQTT – a machine-to-machine publish/subscribe messaging transport protocol. It is light weight, open, simple, and designed so as to be easy to implement.
A Raspberry Pi uses Node-Red to listen to Twitter, and picks out any Tweets containing the hashtag #FeelBot, and forwards any of the emotions FeelBot can feel to the MQTT broker.
Tweet an emotion to #FeelBot, and FeelBots all over the world will react in sympathy.

“I feel a bit sad, #FeelBot”

FeelBot and mental health

FeelBot isn’t designed to solve the world’s mental health problems. What it can do is use a little 'nudge psychology' to encourage a more open attitude to discussing feelings and emotions. Perhaps in a small way FeelBot has a little something to contribute to everyone’s mental health.
