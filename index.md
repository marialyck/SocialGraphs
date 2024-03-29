## Collaboration between artists in a organic network
### 02805 - Social Graphs and Interactions @ The Technical University of Denmark

Group members:

_Hjalte Reuss Schmidt - s163471_

_Phillip Kragh Aagaard - s190736_

_Maria Lyck Carstensen - s144478_

#### For the Explainer Notebook: 
Click here: 

<a href="https://github.com/marialyck/SocialGraphs/blob/master/ExplainerNotebookvFinal.ipynb">Explainer Notebook</a>


### Introduction
Have you ever wondered about all the connected artists on Spotify featuring each other and how they might be connected? Have you ever listened to new music thinking "oh featuring that artist... AGAIN?" You are not alone with that feeling then. We have decided to check it out. So we dug into the Spotify API and found the top connected artists. We dug further into their songs to see if there were a specific way of using the words for these connected artists. And we dug even further and looked to Wikipedia to clear up if there were any similarities between those featuring artists. What we could see from the top artists ie. the ones that most often had a featuring artist with them was mostly the language. It was not for the fainthearted to read. 
### Take a look at the appetizer video
Simply click the image and you will have joyfull music for the rest of your reading.

[![Youtube video example](https://img.youtube.com/vi/kWTqM2rLA7A/0.jpg)](https://www.youtube.com/watch?v=kWTqM2rLA7A&t=5s "The apetiser video")

_The apetiser video, for the dataset_

### Data and API
Information about the data, format, size etc.

- Spotify API (artist and song details)
- Genius API (lyrics)
- Wikipedia API (description on artists)

Download a dataset if you want to play around with the data yourself.

For the full repository

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/marialyck/SocialGraphs/archive/master.zip" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-cloud-download" data-size="large" aria-label="Download marialyck/SocialGraphs on GitHub">Download</a>

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/marialyck/SocialGraphs/tree/master/spotify">Download only the Spotify network</a> 

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/marialyck/SocialGraphs/tree/master/Dataset">Download only lyrics</a>

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/marialyck/SocialGraphs/tree/master/wiki">Download wikipages</a>



### Network: _how is it made?_

The following network is made upon a organic structure.

Artist | *Pitbull* | *Major Lazer* | *Gucci Mane* | *Too Short* | *San Quinn*
------------ | ------------ | ------------- | ------------- | ------------- | -------------
*Pitbull* | 0 | 2 | 2 | 3 | 3
*Major Lazer* | 2 | 0 | 2 | 3 | 4
*Gucci Mane* | 2 | 2 | 0 | 2 | 3
*Too Short* | 2 | 3 | 2 | 0 | 1
*San Quinn* |2 | 3 | 1 | 2 | 0

_Fig 2.2: Network graph_

But let us first have a look at an interactive view of the full featuring artist network

<embed src="https://severin.edea.dk/Temp/index.html" width="1200" height="800">
_note that you might be able to scroll in graph._

Look around a bit and maybe even get an idea of how connected the nodes are to each other. We have kindly removed the ones that were not connected. Simply because this network that we are going to analyse is all about who is the most connected artist. This is certainly not the one without any connections. Saying connections we really mean featuring. 

### Network: Analysis
Looking into the network and all the details to try to figure out what makes these artist so special. We tried to make a graph of the in and out degrees. Beside the comparisons made between the analyzed nodes, i.e. the nodes with highest total degrees, a lot of insights about the collaborating nature of musicians can be gained from network or graph analysis.


![Image of Yaktocat](network_analysis/DegreeDistribution_acutal_scale.png)

In well accordens with what was found before the medians are found to be 1 and 0 for the in- and out-degrees, respectively, showing that most artists are only little linked to their fellow artists.

The right-skewness of these ditributions, i.e. occurence of many little connected nodes combined with a few very connected nodes (hubs), is a good indication that the network indeed is a real network. This was expected so let's continue the analysis. 


We also investigated whether any correlations could be found between the in- and out-degrees. However, as seen from the scatter-plot below, there does generally not seem to be any such correlations.

![Image of Yaktocat](network_analysis/InOutScatter.png)



### Audio Analysis
The different categories of music in Spotify is quite interesting to take a look at when it comes to the generated network. Later on considering the wordclouds and the sentiment analysis it can be interesting to remember a parameter such as dancability. Without revealing what the words of the artist Too $Short is like - it might come as a surprise for some that these apparently are danceable lyrics. 
![Image of Yaktocat](audio_analysis/AudioFeatures.png)

### Text Analysis
The text analysis contains information from lyrics and Wikipedia page on artits. The course of action is that the 5 chosen artist from the network is then being used to collect 5 songs from each artist. These songs words will then be analyzed to see if the artist are using the same words and which words are more specific to one artist.

#### Cleaning the text for further analysis
The first step in order to analyze text in this case both lyrics and text from Wikipedia, the text files must be "cleaned" to get the best result further on. By cleaning the purpose is to remove, punctuations (!?:;., etc.) this includes do not helps us, so those signs are removed. All words are being transformed into lower case, this helps to not being confused if the same word are written with full lower case or just the first letter is capital, this mistake are being avoided by simple removing the all capital letters and replacing them with lower case. Also stopwords are removed in order to focus on the specific words used by the artist or about the artist. Stopwords includes I, all, we, where and so on. The lyrics which are merged into one text file per artist contains square brackets just before a verse, to indicate which verse and who is performining that verse. This data is also removed. 

#### Starting to analyze the text
The initial plan is to see which words are mostly being used by an artist. This can be described as if all five artist repeatly singing a word, this word are not that interesting for us, therefor we perform what is called TF-IFD. This is term frequency–inverse document frequency, which describes first how important a word is in porpotion to the overall corpsus'. Then we calculate how offen this word is in a document or corpus in propotion to how many corpus there are in total. If a word appears in all corpurs', the lower the word will score. 

When the TF-IDF is calculated the result can then be used to create a visual representation of the words which just have been calculated. To illustrate this a wordcloud is a truly great option. The wordcloud features to show a given amount of words, these words' size depends on the result from previous calculation. To the larger the word is, the greater the value is. 

In this project, TF-IDF and wordclouds has been used to show which words are being writing into the respective artist lyrics. 

The first artist is Major Lazer. 

#### Major Lazer 
The first wordcloud is based on analysis from the groups lyrics (5 songs).

![Image of Yaktocat](img/majorlazer/majorlazer_wordcloud_lyrics.png)

_Fig x.x: Wordcloud of 5 songs words from artits Major Lazer._

The words which are represented with the biggest font size, would be _behaving, kiss, wine and clang_. 
An interesting comparison is to compare the words from the wordcloud with the top 10 words being used in the 5 chosen songs. 

![Image of Yaktocat](img/majorlazer/majorlazer_top10_lyrics.png)

_Fig x.x: Top 10 most used words from artits Major Lazer's 5 chosen songs._

First, it seems to match, that the words from the wordclouds are similiar to the graph illustrating word count. This might result in that, these words are more likely to be used by Major Lazer than any of the 4 other artist.

Next one interesting analysis was to see if there are any similiarity between the artists lyrics and what people are writing about them on Wikipedia. In order to do this, the same process of cleaning the data has been made. After cleaning the data TF-IDF could be calculated to render a wordcloud based on data from Wikipedia. 

![Image of Yaktocat](img/majorlazer/majorlazer_wordcloud_wiki.png)

_Fig x.x: Wordcloud of information from artits Major Lazer's Wikipedia page._

And together with that worldcloud a graph that shows the wordcount can be seen.

![Image of Yaktocat](img/majorlazer/majorlazer_top10_wiki.png)

_Fig x.x: Top 10 most used words from artits Major Lazer's Wikipedia page._

Just to compare the two different wordclouds and graphs, the words on the wordcloud from wikipedia are more genereal inspirational and more likely to be glad words.

#### Gucci Mane
Next artits which have been a part of the lyrics analysis, is Gucci Mane. The same process as the lyrics from Major Lazer, has been applied to Gucci Mane's 5 songs which has been chosen. First is the wordcloud based on TF-IDF calculation.

![Image of Yaktocat](img/guccimane/guccimane_wordcloud_lyrics.png)

_Fig x.x: Wordcloud of 5 songs words from artits Gucci Mane._

To briefly sum of some of the words shown in figure x.x, the word which scored the highest score from the TF-IFD was _Gucci_ which also is part of the artist name. But this might also be a reference to the luxury brand _Gucci_ which makes clothes, bags and accessories. To compare the wordcloud with word counts, a graph is made to illustrate which words are being used most.

![Image of Yaktocat](img/guccimane/guccimane_top10_lyrics.png)

_Fig x.x: Top 10 most used words from artits Gucci Mane's 5 chosen songs._

_The word which has been deleted due to explicit content._

When comparing both the wordcloud with word counter, it is not clearly the same words which are presented. The word counts are in generel the most commen words by Gucci Mane within in chosen 5 songs. Where the words from the wordcloud is more weighted, in context that if some of the words appears in all 5 artist songs, it will then score a lower score, where if the words only appears in one artist song, the score would be significantly higher. 

The text is again being compared to the artist's Wikipedia page.

![Image of Yaktocat](img/guccimane/guccimane_wordcloud_wiki.png)

_Fig x.x: Wordcloud of information from artits Gucci Mane's Wikipedia page._

The top 10 wordcounts are illustrated into a graph figure x.x.

![Image of Yaktocat](img/guccimane/guccimane_top10_wiki.png)

_Fig x.x: Top 10 most used words from artits Gucci Mane's Wikipedia page._

#### San Quinn
San Quinn is another artist that popped out in the network. To get a grasp of what kind of artist he is a wordcloud based on the TF-IDF calculations is created. The wordcloud is based on 5 of San Quinn's songs.

![Image of Yaktocat](img/sanquinn/sanquinn_wordcloud_lyrics.png)

_Fig x.x: Wordcloud of 5 songs words from artits San Quinn._

Considering the word cloud one might see that it is not a soft pop artist. But it becomes even more clear when looking to his top 2 most used words. To sum up and give an overview the words are counted and the 10 most used are shown below in the graph.

![Image of Yaktocat](img/sanquinn/sanquinn_top10_lyrics.png)

_Fig x.x: Top 10 most used words from artits San Quinn's 5 chosen songs._

_The word which has been deleted due to explicit content._

When comparing both the wordcloud with word counter, it is not clearly the same words which are presented. The word counts are in generel the most commen words by Gucci Mane within in chosen 5 songs. Where the words from the wordcloud is more weighted, in context that if some of the words appears in all 5 artist songs, it will then score a lower score, where if the words only appears in one artist song, the score would be significantly higher. 

The text is again being compared to the artist's Wikipedia page.

![Image of Yaktocat](img/sanquinn/sanquinn_wordcloud_wiki.png)

_Fig x.x: Wordcloud of information from artits San Quinn's Wikipedia page._

To get an idea og his top most used words it is counted again and shown as a diagram below. 

The top 10 wordcounts are illustrated into a graph figure x.x.

![Image of Yaktocat](img/sanquinn/sanquinn_top10_wiki.png)

_Fig x.x: Top 10 most used words from artits San Quinn's Wikipedia page._

#### Pitbull
Pitbull seems to have a less cursing wordcloud though the words are still rather harsh. Taking into considerations that this is the third artist popping out in the network as the most connected artist one might start to wonder if the road to success is a really hard and negative language. However it will be left to the sentiment analysis to conclude that.

The wordcloud based on Pitbulls 5 songs looked like this when done rendering.

![Image of Yaktocat](img/pitbull/pitbull_wordcloud_lyrics.png)

_Fig x.x: Wordcloud of 5 songs words from artits Pitbull._

Considering the word cloud one might see that it is not a soft pop artist. But it becomes even more clear when looking to his top 2 most used words. To sum up and give an overview the words are counted and the 10 most used are shown below in the graph.

![Image of Yaktocat](img/pitbull/pitbull_top10_lyrics.png)

_Fig x.x: Top 10 most used words from artits Pitbull's 5 chosen songs._

_The word which has been deleted due to explicit content._

When comparing both the wordcloud with word counter, it is not clearly the same words which are presented. The word counts are in generel the most commen words by Gucci Mane within in chosen 5 songs. Where the words from the wordcloud is more weighted, in context that if some of the words appears in all 5 artist songs, it will then score a lower score, where if the words only appears in one artist song, the score would be significantly higher. 

The text is again being compared to the artist's Wikipedia page.

![Image of Yaktocat](img/pitbull/pitbull_wordcloud_wiki.png)

_Fig x.x: Wordcloud of information from artits Pitbull's Wikipedia page._

The top 10 wordcounts are illustrated into a graph figure x.x.

![Image of Yaktocat](img/pitbull/pitbull_top10_wiki.png)

_Fig x.x: Top 10 most used words from artits Pitbull's Wikipedia page._

#### Too $hort
This is interesting. Too $Short was not a namee that rang many bells so creating the wordcloud was a surprise and what a surprise. Giving all the wordclouds a glampse so far - this word cloud is by far the one containing the most female names and rude words. 
Again 5 lyrics went into a TF-IDF analysis out came a rude wordcloud.

![Image of Yaktocat](img/tooshort/tooshort_wordcloud_lyrics.png)

_Fig x.x: Wordcloud of 5 songs words from artits Too $hort._

So let us take a look at the top 10 and see if that is any better. And it is quite clear to see that we are dealing with an artist that uses hard language as a way of making music. 

![Image of Yaktocat](img/tooshort/tooshort_top10_lyrics.png)

_Fig x.x: Top 10 most used words from artits Too $hort's 5 chosen songs._

_The word which has been deleted due to explicit content._

It is clear to see that the top used words matches the artist language in the wordcloud. 

The text is again being compared to the artist's Wikipedia page.

![Image of Yaktocat](img/tooshort/tooshort_wordcloud_wiki.png)

_Fig x.x: Wordcloud of information from artits Too $hort's Wikipedia page._

The top 10 wordcounts are illustrated into a graph figure x.x. 

![Image of Yaktocat](img/tooshort/tooshort_top10_wiki.png)

_Fig x.x: Top 10 most used words from artits Too $hort's Wikipedia page._


### Sentiment Analysis
What is interesting when working with a lot of text is to see whether it is overall positive or negative and since looking at the wordclouds one might have an idea that the lyrics as well as the Wikipedia site is overall negative considering some of the hard words. With a sentiment analysis it is possible to get an idea of just that. The higher the words are rated in the histogram the more negative the words used.


#### Gucci Mane
Gucci Mane has several larger words in his wordcloud that is considered negative. Looking to just the lyrics now the histogram below confirms the rather negative language. 

![Image of Yaktocat](img/guccimane/Guccimane_sentiment.png)


So what would be interesting to take a look at now is whether the wikipedia page is supporting this negative language style. If wikipedia objectively describes Gucci Mane, they might be forced to use some of the words. And a dark history could also contribute to a darker sentiment analysis. 

Words like "jail" and "trap" do not pop out as positive in the sentiment analysis so showing the two graphs together might give an idea of the sentimental analysis of the lyrics and the Wiki-page.

![Image of Yaktocat](img/guccimane/guccimane_wiki_lyric.png)

So looking into the next one, one should now pay attention to the y-axis. The amount of words are really changing from one artist to the next and this is worth noticing in order to get the right image of the artist.

Major Lazer has remarkable few words when compared to Gucci Mane. The Wiki page seems to be almost empty compared to the above artist.
![Image of Yaktocat](img/majorlazer/MajorLazer_sentiment.png)
Looking to the wikipedia page, one might get the idea that the y are more similar than Gucci Mane, but this seems to be a case of y-axis confusion. 
Take a look at the y-axis and reconsider. 
![Image of Yaktocat](img/majorlazer/majorlazer_wiki_lyric.png)

Looking to the bad boy of the class room, at least if we consider the wordcloud, Too $horts analysis is definitely to the lower end than the others we have seen so far. More words are to be found around 0 than if we take a comparison with one of the others (don't worry, we will do that in just a second.)
![Image of Yaktocat](img/tooshort/TooShort_sentiment.png)

The wikipage seems to follow the trend, too $hort is not a possitive happy fairy. 
![Image of Yaktocat](img/tooshort/tooshort_wiki_lyric.png)

And the second has passed. Try to see how Pitbull's analysis vs. Too $hort looks like. The lowest scores are the negative words. And the words scoring 10 are words like peace, harmony and rainbows and uniconrns (Think you get the picture)
![Image of Yaktocat](img/PitBullTooShortsentiment.png)

Now we cheated a bit and already looked to Pitbull - it seems like there are still a lot of hard words going on, but there are more in the middle than eg. Too $hort had. 
![Image of Yaktocat](img/pitbull/Pitbull_sentiment.png)

The wiki page gives an impression of a rather large amount of words were the feelings is a bit mixed. It is most certainly not all positive. 
![Image of Yaktocat](img/pitbull/pitbull_wiki_lyric.png)

So what we can say about San Quinn's analysis of the sentiments is that he stands out like a rather negative person as well. However thinking about the rather negative analysis we had here we might wantto consider which category has the most featuring artists.
![Image of Yaktocat](img/sanquinn/SanQuinn1_sentiment.png)

San Quinn has almost no words on his wikipedia site, so the small bars indicates that rather well. However the words that are present are certainly mostly negative. 
![Image of Yaktocat](img/sanquinn/sanquinn_wiki_lyric.png)
 
### Conclusion
First of all some surprises occured along the way. This is most likely how it is when working with a completely new, not knowing what to expect, network. Who would have guessed that the friendship paradox would come out with such a low degree? Looking to the network it did come as a surprise. 

Considering the wordclouds and the sentiment analysis the language did not come as a surprise. The 5 top artists were mostly in rap or harder versions of pop music and it seems to be that genre that has the most collaborations between artists. The explanation to the hard language is therefor rather explanable. 

For future analysist one might find it funny to see what words would make a song popular or where to be on the audioanalysist. Some might believe that a popular song is a song with high danceability. However we used our effort into getting the idea of how songs are formed and we got a pretty good idea about that.



